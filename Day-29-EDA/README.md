# Day 29 – Google Play Store EDA & Feature Engineering

## Dataset
[Google Play Store Apps](https://www.kaggle.com/datasets/lava18/google-play-store-apps) [web:475]

## EDA Process
1. **Data Loading & Cleaning**
   - Fixed data types (Installs, Price, Reviews)
   - Handled missing values (Category, Rating)

2. **Univariate Analysis**
   - App categories distribution
   - Ratings histogram (skewed right)
   - Installs log-scale plot

3. **Bivariate Analysis**
   - Category vs. Average Rating
   - Size vs. Installs correlation
   - Content Rating vs. Installs

4. **Feature Engineering**
   - `installs_per_review = Installs / Reviews`
   - `paid = Price > 0`
   - Log transformation for skewed features

