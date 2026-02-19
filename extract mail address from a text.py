import re
from typing import List


def extract_emails(text: str) -> List[str]:
    """
    Extract all valid email addresses from a given text string.

    Args:
        text (str): Input text containing zero or more email addresses.

    Returns:
        List[str]: List of extracted email addresses.
    """
    pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    return re.findall(pattern, text)


# -------------------------
# Example Usage
# -------------------------
if __name__ == "__main__":
    sample_text = """
    Please contact:
    - john.doe+ran@5g-network.co.jp
    - ops_team-1@core-system.io
    Invalid emails:
    - user@@domain..com
    - test@.com
    """

    emails = extract_emails(sample_text)

    print("Extracted email addresses:")
    for email in emails:
        print(email)
