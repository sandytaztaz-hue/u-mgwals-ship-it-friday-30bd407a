import os

# Deterministic: writes the same single commit line on every run.
# One concrete Friday scene (4:59 p.m. push), one real number (47 files),
# one named object (the laptop tests), punchline last.
LINE = "fix(deploy): pushed 47 files to prod at 4:59 p.m. Friday — tests passed on my laptop, so the outage is a surprise for all of us"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
