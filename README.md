<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#fbbf24&height=180&section=header&text=ZIP%20Safety%20Check&fontSize=42&fontColor=ffffff" alt="ZIP Safety Check banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=FBBF24&center=true&vCenter=true&width=650&lines=Inspect%20archives%20before%20you%20unpack%20them." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/zip-safety-check?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/zip-safety-check?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/zip-safety-check?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/zip-safety-check?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="ZIP Safety Check illustration"/></p>

## 🚀 Overview

ZIP Safety Check performs a read-only inspection of ZIP members before extraction. It flags unsafe paths, symlink entries, duplicate normalized names, and archive-bomb warning signs while leaving the archive untouched.

## ✨ Features

- 📦 Inspect ZIP entries without extracting them
- 🚫 Detect absolute paths and parent-directory traversal
- 🔗 Flag symlink entries and duplicate destinations
- 📏 Warn about extreme compression ratios and oversized archives

## 🎬 Demo

~~~bash
python main.py download.zip --max-ratio 100
~~~

The tool reads archive metadata only and never extracts files.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/zip-safety-check.git
cd zip-safety-check
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
zip-safety-check/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#fbbf24,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
