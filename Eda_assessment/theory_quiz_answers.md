# Part 2 — Theory Quiz Answers

### Question 1
**What are the two separate pieces that make up a running notebook, and which one holds your variables in memory?**

**Answer:**  
A running notebook consists of the **Frontend Interface** (the web-based UI editor) and the **Kernel** (the underlying Python execution engine). The **Kernel** holds all variables, functions, and state in memory.

---

### Question 2
**You run `arr.mean(axis=0)` and get back a single number instead of an array of per-column means. What does that tell you about `arr`'s shape, and how would you check?**

**Answer:**  
This indicates that `arr` is a **1-dimensional array** (vector), as computing the mean along `axis=0` reduces a 1D array to a scalar. You can verify this by checking `arr.shape` or `arr.ndim`.

---

### Question 3
**Why does `df[(df['a'] > 5) and (df['b'] < 10)]` raise an error (or behave unexpectedly) instead of just working like the equivalent plain-Python condition?**

**Answer:**  
The Python `and` operator evaluates the overall truthiness of an entire object using `bool()`, which pandas disallows for multi-element Series because it is truth-value ambiguous. Element-wise logical evaluation in pandas requires the bitwise `&` operator with parentheses around each condition: `df[(df['a'] > 5) & (df['b'] < 10)]`.

---

### Question 4
**You reshape a NumPy array and then change a value in the reshaped version — the original array also changes. Explain why, in terms of what `.reshape()` actually returns.**

**Answer:**  
`.reshape()` returns a **view** of the original array rather than a copy. Both the original and reshaped arrays share the exact same underlying buffer in physical memory, so modifying elements in one affects the other.

---

### Question 5
**A column has 40% of its values missing. Give one real argument for `dropna()` and one real argument for `fillna()` on that same column — the "right" answer depends on what, specifically?**

**Answer:**  
* **Argument for `dropna()`:** Imputing 40% of a column risks introducing significant synthetic bias or artificial patterns into the dataset.  
* **Argument for `fillna()`:** Dropping 40% of the rows causes severe data loss, discarding valuable real information present across all other columns in those rows.  
* **Key Decision Factor:** The "right" answer depends on whether the data is Missing Completely at Random (MCAR) versus systematically missing, and how critical the feature and sample size are to the downstream analysis or model.

---

### Question 6
**Why is `df['total'] = df['price'] * df['qty']` faster than the equivalent `.apply(lambda row: row['price'] * row['qty'], axis=1)` — what's actually different about how each one runs?**

**Answer:**  
Vectorized multiplication (`df['price'] * df['qty']`) delegates element-wise math directly to compiled C routines that operate on contiguous memory blocks via NumPy. In contrast, `.apply(axis=1)` iterates row-by-row in pure Python, creating a pandas Series object for every row and incurring significant Python interpreter and dynamic type-checking overhead.

---

### Question 7
**You need to compare average resolution time across four categories. Name the correct plot type for that specific question, and explain what a line chart would incorrectly imply if used instead.**

**Answer:**  
The correct plot type is a **Bar Chart**. Using a line chart would incorrectly imply a continuous trend, ordering, or functional relationship between discrete, independent categories.

---

### Question 8
**Describe one concrete way to make a real chart misleading without changing any of the underlying data.**

**Answer:**  
Truncating the Y-axis (for example, starting a bar chart Y-axis at 85 instead of 0) visually exaggerates minor numerical differences, making tiny relative variations appear disproportionately massive.
