# Security Policy

## Supported Versions

The following versions of this project are currently supported with security updates:

| Version | Supported          |
| ------- | ------------------ |
| `main`  | ✅ Yes             |
| Older branches | ❌ No     |

We recommend always using the latest version of this template.

---

## Reporting a Vulnerability

We take security seriously, even for open source website templates. If you discover a vulnerability — including issues related to dependency exposure, script injection, or unsafe configuration defaults — please report it responsibly.

### How to Report

**Please do not open a public GitHub issue for security vulnerabilities.**

Instead, report vulnerabilities privately via one of the following:

- **GitHub Private Vulnerability Reporting** *(preferred)*: Use the [Security tab](../../security/advisories/new) on this repository to submit a private advisory.
- **Email**: If GitHub's private reporting is unavailable, contact the maintainer directly at the email listed in the repository profile.

### What to Include

To help us triage and resolve the issue quickly, please include:

- A clear description of the vulnerability
- Steps to reproduce or a proof-of-concept (if applicable)
- The potential impact or attack scenario
- Any suggested mitigations (optional but appreciated)

---

## Response Process

After receiving your report, we will:

1. **Acknowledge** your report within **48 hours**
2. **Assess** the severity and scope of the issue
3. **Develop and test** a fix, coordinating with you if needed
4. **Release a patch** and credit you in the changelog (unless you prefer to remain anonymous)
5. **Publish a security advisory** if the severity warrants it

---

## Scope

This is a **static website template**. The primary security considerations include:

- Third-party dependencies (npm packages, CDN scripts)
- Configuration files that users may expose sensitive data through
- Cross-site scripting (XSS) risks in any templating or rendering logic
- Insecure defaults in deployment configurations

Issues related to a **user's own deployment** (e.g., their hosting environment or custom modifications) are outside the scope of this project's security responsibility.

---

## Disclosure Policy

We follow a **coordinated disclosure** model. We ask that you give us reasonable time to address a confirmed vulnerability before any public disclosure. We aim to resolve critical issues within **14 days** and will communicate timelines transparently.

---

## Acknowledgements

We appreciate the security research community and responsible reporters who help keep open source projects safe. Contributors who responsibly disclose valid vulnerabilities may be acknowledged in our release notes.

---

*This security policy was last updated: March 2026.*
