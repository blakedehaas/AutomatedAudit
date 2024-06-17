"""
Configuration file for the Automated Audit.

This file contains configurations for:
- The list of repositories to audit
- The directory path template for the repositories
- Document generation settings
- The list of terms to audit
- The grep command template

Ensure the `terms` list contains the terms you want to audit.
Ensure you have cloned the repositories you want to audit into the directory specified by `repositoryDirectory`.
"""

# Configure terms to audit
terms = ["term1", "term2", "term3"]

# Configure repository list to audit
repositoryDirectory = "repositories"

# Configure document
documentFolder = "Audit"
documentHeadingTemplate = "Audit - {}"
defaultAction = "TBD"
defaultJustification = "TBD"

# Configure grep command
grepCommandTemplate = 'grep -rniw {path} -e "{term}"'
