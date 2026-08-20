# Orders Data — Technical Summary

## 1. Overview

This report covers an analysis of an e-commerce orders dataset: 5,015 order
records spanning January 2024 onward, one row per order. Each order includes an
order ID, timestamp, customer ID, product category, quantity, unit price, and
region. Before any analysis, the data was checked for quality problems and
cleaned; this document explains what was found, what was done about it, what
the cleaned data shows, and what still isn't fully resolved.

## 2. What was wrong with the raw data, and how we found it

The raw dataset was checked using standard diagnostic steps — a structural
summary, a missing-value count, and frequency counts on the category-type
columns — before any values were changed. That check turned up six distinct
problems:

| Problem | Scope | How it was found |
|---|---|---|
| Missing customer ID | 150 orders (~3%) | Missing-value count |
| Missing region | ~200 orders (~4%) | Missing-value count |
| Inconsistent category spelling ("Electronics" vs. "electronics") | Affects the Electronics category count | Frequency count on `product_category` |
| Negative quantities | 30 orders | Direct check, since a missing-value count doesn't catch a present-but-invalid number |
| Negative unit prices| Minimum value of -$25.58 | Summary statistics (min check on unit_price) |
| Repeated, implausible unit price ($4,999.99) | 21 orders in the raw data (20 originally planted, plus one row that got duplicated) | Direct check for the repeated value |
| Duplicate order records | 15 orders | Row-level duplicate check |

A note on that price count: the diagnosis write-up in the working notebook
initially said 20 rows had the $4,999.99 price, but the code's own output
showed 21. The discrepancy traces back to how the dataset was built — the 15
duplicated rows were sampled *after* the outlier prices were already planted,
so one of the 20 original outlier rows ended up duplicated, bringing the raw
total to 21. This is now corrected in the written diagnosis.

## 3. How each problem was resolved

Each problem was handled individually rather than with one blanket rule,
since a missing customer ID and an implausible price aren't the same kind of
issue and don't call for the same fix.

- **Missing customer ID (150 orders):** Dropped. There's no reliable way to
  infer who placed an order with no ID on record, and it's a small share of
  the data (~3%), so removing those rows was preferred over guessing.
- **Missing region (~200 orders):** Filled with the label "Unknown" instead of
  dropped. Region isn't essential to whether an order itself is valid, so
  keeping the row and marking the gap explicitly preserves more usable data
  than discarding it.
- **Inconsistent category spelling:** Standardized casing so "Electronics" and
  "electronics" count as one category instead of two.
- **Negative quantities (30 orders):** Converted to positive values and
  separately flagged as returns (a new `is_return` column), rather than
  dropped. A negative quantity most plausibly represents a return recorded
  with the wrong sign, not a meaningless number — the order itself is real.
- **Negative Unit Price:** Converted to positive values using .abs() to correct
  sign-flip data-entry or system logging errors without losing valid order details. 
- **Outlier price of 4,999.99 (20 orders after the customer-ID cleanup
  removed one of the 21):** Replaced with the dataset's median price. This
  value repeats exactly and sits far outside the otherwise normal price
  distribution, which is the signature of a data-entry placeholder rather
  than a real price. Replacing it (instead of dropping the row) keeps the
  order's other valid fields — quantity, category — usable.
- **Duplicate records (15 orders):** Dropped outright, since they were
  confirmed as exact full-row repeats rather than legitimate repeat orders.

After all six fixes, the cleaned dataset has **4,850 orders** and no remaining
missing values, duplicates, or negative quantities.

## 4. What the cleaned data shows

- **Prices cluster around $45 per order**, with a roughly symmetric spread.
  Once the 4,999.99 placeholder values were replaced, the price distribution
  no longer has the artificial spike that was present in the raw data.
- **Order volume is fairly even across the four product categories**
  (Electronics, Home Goods, Apparel, Books) — none dominates the order count
  after the Electronics-spelling fix merged the split counts.
- **Quantity and price don't move together.** Orders of 1 through 7 items
  appear across the full range of prices, with no visible pattern of cheaper
  items being bought in bulk or expensive items being bought in smaller
  amounts.
- **Returns make up a small slice of orders** — 29 orders, or about 0.6% of
  the cleaned dataset — flagged via the negative-quantity fix and worth
  tracking as their own category going forward.
- **Region and category breakdowns are close to evenly split** by design
  (the source data was generated with roughly equal weighting across regions
  and categories), so no single region or category stands out as unusually
  high- or low-volume.

## 5. Known limitations

- **The "Unknown" region and dropped-customer rows are simplifications, not
  real information.** Filling missing regions with "Unknown" and removing
  orders with no customer ID were reasonable, defensible choices — but
  neither recovers the actual missing data. Any regional or per-customer
  breakdown built on this cleaned dataset is working from an incomplete
  picture, not a fully accurate one.
- **A handful of orders still carry a negative unit price** (as low as about
  -25). This wasn't one of the problems the assignment's cleaning checklist
  called for, so it was left as-is rather than fixed. It wasn't caught during
  diagnosis either, since the diagnosis step followed that same checklist —
  which checks for missing values, duplicates, and the specifically named
  issues, none of which a negative-but-present price trips. It's a genuine
  data problem (a price can't logically be negative), just one that fell
  outside this pass's defined scope. Flagging it here rather than silently
  leaving it in the data: a follow-up pass should add an explicit check and
  fix for it.
- **The median-replacement fix for outlier prices assumes the true price was
  "typical."** Replacing 4,999.99 with the median is a reasonable default,
  but it's a guess — the real price for those 20 orders is unknown and could
  have been anything.
