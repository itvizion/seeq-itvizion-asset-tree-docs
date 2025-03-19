# itv_asset_tree
ITV Asset Tree  **ITV Asset Tree** is a Python package designed to streamline the creation and management of asset trees in Seeq. 

---

## 📖 Documentation

To access the full documentation, open:

👉 **[Click Here to Open Docs](docs/build/html/index.html)**

(_If the link doesn't work, navigate to `docs/build/html/index.html` and open it manually._)

---

## **Installation Instructions for `itv_asset_tree`**
### **Prerequisites**
- **Python**: Version **3.11** or higher  
- **pip**: Latest version installed  
- **git**: Installed and configured  

---

## 1. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\\Scripts\\activate`
```

## 2. Install the itv-asset-tree Package directly from the GitHub Repository
```bash
pip install git+https://github.com/itvizion/seeq-itvizion-asset-tree.git
```

## 3. Set Up Environment Variables
Create a `.env` file in the root directory with the following content:
Below is an example...
```ini
SERVER_USERNAME=your_email@example.com
SERVER_PASSWORD=my_passwd
SERVER_HOST=https://your_server_name.seeq.tech
LOG_LEVEL=debug
SEEQ_FORCE_LOGIN=True
```
Update these values according to your server configuration.

## 4. Verify Installation
```bash
itv-asset-tree
```

## Additional Notes:
- **Local Development:** Use `pip install -e .` for editable installs.
    For example:
    - `git clone https://github.com/itvizion/seeq-itvizion-asset-tree.git`
    - `cd seeq-itvizion-asset-tree`
    - `python -m venv venv`
    - `source venv/bin/activate`  # On Windows use `venv\Scripts\activate`
    - `pip install -r requirements.txt`
    - `pip install -e .`

- **Versioning:** Managed by `versioneer`
- **Testing:** Uses `pytest` locally and `pytest-mock` for CI
- **FastAPI:** Find web api at http://127.0.0.1:8000/docs

- **Quotation:** Submit requests for this add-on to sales@itvizion.com

---
You’re all set! 🎉 Start building with `itv_asset_tree`.

## License Agreement
By using this software, you agree to the [IT Vizion EULA](https://itvizion.com/eula).

