# ITV Asset Tree Documentation

This repository contains the standalone documentation for the **ITV Asset Tree** project, a Python-based toolkit for building asset trees to be used in analytics pipelines designed for Seeq's Data Lab environment.

---

## 📚 Documentation Usage

To view the documentation locally:

### 1. Clone this repository

```bash
git clone https://github.com/itvizion/seeq-itvizion-asset-tree-docs.git
cd seeq-itvizion-seeq-itvizion-asset-tree-docs
```

### 2. Set up the environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use venv\\Scripts\\activate
pip install -r requirements.txt
```

> 💡 Ensure you also have access to the source code repository for `itv_asset_tree`. This documentation loads Python modules directly from that external path.

### 3. Start the documentation server

```bash
cd seeq-docs
mkdocs serve
```

Open your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 📦 Alternative Access Methods

If you do not have access to the code repository but still need to view the documentation:

#### Option 1: Open Locally (Offline Use)

1. Unzip the provided documentation package.
2. Open `index.html` in the `site/` folder with any browser.

#### Option 2: Shared Drive or Portal

- Access the unzipped `site/` folder hosted on a network share or company portal.
- Open `index.html` in your browser.

#### Option 3: Local Web Server (Developers Only)

If you want to serve the documentation locally:

```bash
cd seeq-docs/site
python -m http.server 8000
```

Then open: [http://localhost:8000](http://localhost:8000)

---

## 🧭 Structure

Documentation is written in Markdown and rendered using **MkDocs** with the Material theme and mkdocstrings for auto-generating API documentation from Python code.

All modules in the `itv_asset_tree` package are included and grouped by feature domain.

---

## 🛠 Requirements

- Python 3.11+
- Access to the external code repository containing the `itv_asset_tree` package
- See `requirements.txt` for Python dependencies

---

## 📝 Style Guide

To ensure complete documentation coverage, all classes, functions, and methods in `itv_asset_tree` should include [Google-style Python docstrings](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). MkDocs + mkdocstrings will render them automatically.

---

## 🔒 License

This documentation is provided under the [IT Vizion EULA](https://itvizion.com/eula).
