import os

# Pigeon Pitch, One Line — one original pitch line, written for this bounty.
ENTRY = "We're disrupting breadcrumbs: one app, every park bench, zero rent — my team already loiters there daily, we just need your seed money to monetize the crumbs."

def main():
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry length must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(text.encode("utf-8"))

if __name__ == "__main__":
    main()
