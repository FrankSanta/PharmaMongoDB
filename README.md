# 💊 Medicines Dataset Analysis with MongoDB

This project analyzes and queries a large-scale dataset of Indian medicines using **MongoDB**. Developed for the *Systems and Methods for Big and Unstructured Data* course at Politecnico di Milano, it demonstrates how document-oriented databases can be leveraged for complex and heterogeneous healthcare data.

---

## 📦 Dataset

The dataset contains structured information about medications, including:
- **Product details**: name, subcategory, manufacturer, price (in INR), and description  
- **Salt composition**: active ingredients and corresponding doses  
- **Side effects**: as a list of medical effects  
- **Drug interactions**: including involved drugs, associated brands, and severity levels

🗂 **Source**: [Kaggle – India Drugs Dataset](https://www.kaggle.com/datasets/knightbearr/india-drugs-dataset)  
📥 Please download the CSV from Kaggle and place it in the working directory before running the pipeline.

---

## 🔄 Data Wrangling

All transformations are handled in `data_wrangling.py`. Key processing steps include:
- **Price Conversion**: Remove currency symbols and cast to float  
- **Side Effects**: Parse comma-separated text into arrays  
- **Salt Composition**: Convert to subdocuments with `composition` and `dose` fields  
- **Drug Interactions**: Restructure into arrays of objects with `drug`, `brand` (as a list), and `effect`  
- **Brands**: Convert single/multiple brand strings into consistent lists  

The final output is a JSON-formatted dataset compatible with MongoDB's document model.

---

## 🧪 Querying the Data

The `queries.txt` file includes **20 complex MongoDB queries** designed to:
- Filter medications by specific components, dosage, price, and manufacturers  
- Identify interactions with critical severity levels like “SERIOUS” or “LIFE-THREATENING”  
- Analyze drug compositions and their side effects  
- Rank manufacturers by price or product count  
- Aggregate by subcategory, brand, or interaction attributes

Queries use `find()`, `$match`, `$group`, `$unwind`, `$sort`, and `$aggregate` operators.

---

## 🚀 How to Run

### 1️⃣ Requirements
- Python 3.x  
- MongoDB (local instance or Docker container)  
- Required Python libraries: `pandas`, `json`

### 2️⃣ Steps

1. **Download the dataset** from Kaggle and place the CSV in your project directory  
2. **Run the wrangling script**:
   ```bash
   python data_wrangling.py
3. **Import into MongoDB**:
   ```bash
   mongoimport --db medicines_db --collection medicine_data --file processed_data.json --jsonArray
4. **Run queries** using MongoDB shell, MongoDB Compass (GUI), or any MongoDB-compatible interface, loading them from queries.txt

---

## 👥 Authors

This project was developed by:

- **Francesca Pia Panaccione** 
- **Francesco Santambrogio**

🎓 *Politecnico di Milano*  
Academic Year: **2023–2024**  
Course: *Systems and Methods for Big and Unstructured Data*
