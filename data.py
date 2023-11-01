feedback_messages = {
    5: [
        "Outstanding! You've mastered the content flawlessly.",
        "Perfection at its best! Keep up the impressive work.",
        "A full sweep! Your preparation is evident in your score.",
        "Bravo! You've showcased a deep understanding of the material.",
        "Incredible performance! Keep holding the standard high."
    ],
    4: [
        "Great job! You're on the brink of perfection.",
        "Just a step away from the top! Your hard work is showing.",
        "A commendable performance! You're very close to a perfect score.",
        "Nearly there! Your efforts have truly paid off.",
        "Keep it up! A little more push and you'll ace it."
    ],
    3: [
        "A solid effort! With a bit more focus, you can reach the top.",
        "You're on the right track! A little more review, and you'll be there.",
        "Good job! A bit more practice will make a big difference.",
        "Showing promise! Consistency will elevate your score.",
        "Keep going! Your grasp on the content is commendable."
    ],
    2: [
        "You've got the foundation! Let's build on it with some more study.",
        "There's potential! A bit more dedication, and you can soar higher.",
        "You're getting there! Keep pushing forward and reviewing your material.",
        "Every effort counts! Dive deeper into the subjects.",
        "You're making progress! Every challenge is an opportunity to learn."
    ],
    1: [
        "It's a start! Remember, every expert was once a beginner.",
        "Let's use this as a stepping stone towards improvement.",
        "Don't be disheartened; focus on your weak points and you'll see growth.",
        "One step at a time! Recognize your strengths and work on your areas of improvement.",
        "Keep your spirit high! Every attempt is a lesson learned."
    ],
    0: [
        "Tough luck! It's a learning curve, and we all have to start somewhere.",
        "Use this as a motivation to come back stronger.",
        "Every setback is a setup for a comeback. Let's review and prepare again.",
        "Never give up! Understanding where you went wrong is the first step to improvement.",
        "Embrace the journey! With perseverance, you'll see the results."
    ]
}

exams = {
    "CFA Level 1": {
        "QUANTITATIVE METHODS": {
            "Rates and Returns": {
                "questions": [
    "Which of the following best describes an interest rate?",
    "An interest rate from which the inflation premium has been subtracted is known as a:",
    "Which return measure is used to compound the rate of returns over multiple periods?",
    "The money-weighted rate of return is the:",
    "Which return measure is used to calculate the average share cost from periodic purchases in a fixed money amount?",
    "Interest rates and market returns are typically:",
    "Gross return refers to the total return on a security portfolio:",
    "Which of the following return measures is used to decrease the effect of outliers?",
    "The real risk-free rate reflects:",
    "A continuously compounded return from t = 0 to t = 2 is:",
    "Net return refers to the return:",
    "Real return is the increase in an investor’s purchasing power, roughly equal to:",
    "If funds are added to a portfolio just before a period of poor performance, which return will be lower?",
    "Which of the following is NOT a component of a nominal interest rate?",
    "The time-weighted rate of return measures:",
    "Which of the following return measures is used to reduce the effect of outliers?",
    "A saver deposits $100 into a bank account. After 90 days, the account balance is:",
    "Which of the following best describes the real risk-free rate?",
    "Which of the following return measures is used to measure an investment’s return over a specific period?",
    "If a stock's initial price is 20 and its price increases to 23, its continuously compounded rate of return is closest to:"
],
                "choices": [
    ["A. A measure of risk or a required rate of return.", "B. A discount rate or a measure of risk.", "C. A required rate of return or the opportunity cost of consumption."],
    ["A. Real interest rate.", "B. Risk-free interest rate.", "C. Real risk-free interest rate."],
    ["A. Arithmetic mean.", "B. Geometric mean.", "C. Harmonic mean."],
    ["A. Average return over a specific period.", "B. IRR calculated using periodic cash flows.", "C. Compound growth rate over a specified horizon."],
    ["A. Arithmetic mean.", "B. Geometric mean.", "C. Harmonic mean."],
    ["A. Stated on a semi-annual basis.", "B. Stated on a quarterly basis.", "C. Stated on an annualized basis."],
    ["A. After deducting fees for management and administration.", "B. Before deducting fees for management and administration.", "C. After deducting commissions on trades."],
    ["A. Arithmetic mean.", "B. Harmonic mean.", "C. Trimmed or winsorized mean."],
    ["A. Time preference for present goods versus future goods.", "B. Expected inflation rate.", "C. Default risk premium."],
    ["A. The sum of the continuously compounded return from t = 0 to t = 1 and t = 1 to t = 2.", "B. The average of the continuously compounded returns over the two periods.", "C. The product of the continuously compounded returns over the two periods."],
    ["A. Before deducting fees for management and administration.", "B. After deducting fees for management and administration.", "C. After adding the inflation rate."],
    ["A. Nominal return minus inflation.", "B. Nominal return plus inflation.", "C. Gross return minus fees."],
    ["A. Time-weighted return.", "B. Money-weighted return.", "C. Both will be the same."],
    ["A. Liquidity premium.", "B. Maturity premium.", "C. Volatility premium."],
    ["A. Simple average of a series of periodic returns.", "B. Compound growth over a specified performance horizon.", "C. Average share cost from periodic purchases in a fixed money amount."],
    ["A. Arithmetic mean.", "B. Harmonic mean.", "C. Trimmed or winsorized mean."],
    ["A. Less than $100.", "B. Equal to $100.", "C. More than $100."],
    ["A. Reflects time preference for present goods versus future goods.", "B. Reflects expected inflation rate.", "C. Reflects default risk premium."],
    ["A. Arithmetic mean return.", "B. Geometric mean return.", "C. Holding period return."],
    ["A. 13.64%.", "B. 13.98%.", "C. 15.00%."]
],
                "answers": [
    "C. A required rate of return or the opportunity cost of consumption.",
    "A. Real interest rate.",
    "B. Geometric mean.",
    "B. IRR calculated using periodic cash flows.",
    "C. Harmonic mean.",
    "C. Stated on an annualized basis.",
    "B. Before deducting fees for management and administration.",
    "C. Trimmed or winsorized mean.",
    "A. Time preference for present goods versus future goods.",
    "A. The sum of the continuously compounded return from t = 0 to t = 1 and t = 1 to t = 2.",
    "B. After deducting fees for management and administration.",
    "A. Nominal return minus inflation.",
    "B. Money-weighted return.",
    "C. Volatility premium.",
    "B. Compound growth over a specified performance horizon.",
    "C. Trimmed or winsorized mean.",
    "C. More than $100.",
    "A. Reflects time preference for present goods versus future goods.",
    "C. Holding period return.",
    "B. 13.98%"
],
                "references": [
    "Page 16",
    "Page 16",
    "Page 16",
    "Page 24",
    "Page 16",
    "Page 25",
    "Page 25",
    "Page 24",
    "Page 24",
    "Page 22",
    "Page 25",
    "Page 25",
    "Page 24",
    "Page 24",
    "Page 24",
    "Page 24",
    "Page 20",
    "Page 24",
    "Page 24",
    "Page 24"
],
            },
            "The Time Value of Money in Finance": {
                "questions": [    "In the context of finance, what is the primary significance of the time value of money?",
    "Which financial calculator is allowed by the CFA Institute for the exam?",
    "What is the primary characteristic of a zero-coupon bond?",
    "How is the price of a zero-coupon bond determined?",
    "What is the primary difference between equity securities and fixed-income securities in terms of cash flows?",
    "For the exam, why is it essential to use a financial calculator when working on time value of money problems?",
    "Preferred stock dividends can be considered to be:",
    "Which of the following best describes the relationship between present values and future values?",
    "The time-weighted rate of return is preferred in the investment management industry primarily because:",
    "If funds are added to a portfolio just before a period of high returns, which return will be higher?",
    "The money-weighted rate of return is the:",
    "Which of the following securities is an example of the time value of money concept?",
    "The required return for equity investors is the:",
    "Which of the following is NOT a primary use of the time value of money in finance?",
    "In the context of time value of money, what does continuous compounding refer to?",
    "Which of the following best describes the cash flow additivity principle?",
    "Which of the following best describes the relationship between the present value and future value of a cash flow when using continuous compounding?",
    "For which type of security is the time value of money concept most straightforwardly illustrated?",
    "Which of the following is a primary difference between equity and fixed-income securities in terms of valuation?",
    "Which of the following best describes the time-weighted rate of return?"
],
                "choices": [
    ["A. It determines the future value of investments.", "B. It reflects the change in purchasing power over time.", "C. It appears throughout various financial instruments and calculations."],
    ["A. Casio FX-991ES", "B. Texas Instruments TI BA II Plus", "C. HP 12C Platinum"],
    ["A. It pays periodic interest.", "B. It is sold at a premium.", "C. It is bought for less than its face value and redeemed at maturity for its face value."],
    ["A. Based on its coupon rate.", "B. By discounting its face value using its yield to maturity.", "C. By adding a premium to its face value."],
    ["A. Equity securities have variable cash flows, while fixed-income securities have fixed cash flows.", "B. Equity securities have fixed cash flows, while fixed-income securities have variable cash flows.", "C. Both equity and fixed-income securities have fixed cash flows."],
    ["A. It ensures accuracy in calculations.", "B. It saves time compared to manual calculations.", "C. It provides a graphical representation of the data."],
    ["A. Variable over time.", "B. Infinite with a fixed stream.", "C. Finite with a variable stream."],
    ["A. Directly proportional.", "B. Inversely proportional.", "C. Not related."],
    ["A. It provides a higher return value.", "B. Portfolio managers typically control the timing of deposits and withdrawals.", "C. Portfolio managers typically do not control the timing of deposits and withdrawals."],
    ["A. Time-weighted return.", "B. Money-weighted return.", "C. Both will be the same."],
    ["A. Average return over a specific period.", "B. IRR calculated using periodic cash flows.", "C. Compound growth rate over a specified horizon."],
    ["A. Common stock with variable dividends.", "B. Zero-coupon bond.", "C. Callable bond with periodic coupons."],
    ["A. Dividend rate.", "B. Yield to maturity.", "C. Discount rate applied to future cash flows."],
    ["A. Calculating the present value of future cash flows.", "B. Determining the face value of a bond.", "C. Inferring a bond's yield from its price."],
    ["A. Compounding at infinite intervals within a year.", "B. Compounding at regular intervals within a year.", "C. Compounding only once at the end of the year."],
    ["A. Cash flows can be added or subtracted regardless of their timing.", "B. Cash flows can only be added if they occur at the same time.", "C. Cash flows from different periods cannot be added directly."],
    ["A. Directly proportional based on the interest rate.", "B. Inversely proportional based on the interest rate.", "C. Directly proportional based on the number of compounding periods."],
    ["A. Equity with variable dividends.", "B. Zero-coupon bond.", "C. Callable bond."],
    ["A. Equity securities are valued based on past dividends.", "B. Fixed-income securities are valued based on future interest payments.", "C. Equity securities are valued based on future cash flows."],
    ["A. It measures the average return over a specific period.", "B. It measures the compound growth rate over a specified horizon.", "C. It is the IRR calculated using periodic cash flows."]
],
                "answers": [
    "C. It appears throughout various financial instruments and calculations.",
    "B. Texas Instruments TI BA II Plus",
    "C. It is bought for less than its face value and redeemed at maturity for its face value.",
    "B. By discounting its face value using its yield to maturity.",
    "A. Equity securities have variable cash flows, while fixed-income securities have fixed cash flows.",
    "B. It saves time compared to manual calculations.",
    "B. Infinite with a fixed stream.",
    "B. Inversely proportional.",
    "C. Portfolio managers typically do not control the timing of deposits and withdrawals.",
    "B. Money-weighted return.",
    "B. IRR calculated using periodic cash flows.",
    "B. Zero-coupon bond.",
    "C. Discount rate applied to future cash flows.",
    "B. Determining the face value of a bond.",
    "A. Compounding at infinite intervals within a year.",
    "B. Cash flows can only be added if they occur at the same time.",
    "A. Directly proportional based on the interest rate.",
    "B. Zero-coupon bond.",
    "C. Equity securities are valued based on future cash flows.",
    "B. It measures the compound growth rate over a specified horizon."
],
                "references": [
    "Page 27",
    "Page 27",
    "Page 28",
    "Page 28",
    "Page 31",
    "Page 27",
    "Page 31",
    "Page 28",
    "Page 19",
    "Page 20",
    "Page 24",
    "Page 28",
    "Page 31",
    "Page 28",
    "Page 28",
    "Page 9",
    "Page 28",
    "Page 28",
    "Page 31",
    "Page 19"
],
            },          
            "Statistical Measures of Asset Returns": {
                "questions": [
    "Which of the following measures identifies the center, or average, of a dataset?",
    "The arithmetic mean is the sum of the observation values divided by:",
    "Which measure is the midpoint of a dataset where the data are arranged in ascending or descending order?",
    "For continuous data, instead of identifying a single outcome as the mode, what is typically identified?",
    "Which measure excludes a stated percentage of the most extreme observations?",
    "Dispersion is defined as the variability around what?",
    "What is the range for the 5-year annualized total returns for five investment managers if the managers’ individual returns were 30%, 12%, 25%, 20%, and 23%?",
    "Which measure of dispersion is the average of the absolute values of the deviations from the arithmetic mean?",
    "Which measure of dispersion is the positive square root of the variance?",
    "What does the coefficient of variation (CV) measure?",
    "Skewness describes the degree to which a distribution is:",
    "A right-skewed distribution has:",
    "For a positively skewed, unimodal distribution, which of the following is true?",
    "Kurtosis measures the:",
    "A distribution that is more peaked than a normal distribution is described as:",
    "Correlation measures the strength of the:",
    "The correlation between two random variables ranges from:",
    "If \( \rho_{XY} \) = 1.0, the random variables have:",
    "If the covariance of X and Y is positive, it indicates that:",
    "Which of the following is a standardized measure of the linear relationship between two variables?"

],
                "choices": [
    ["A) Measures of Dispersion", "B) Measures of Central Tendency", "C) Measures of Skewness", "D) Measures of Kurtosis"],
    ["A) The median of the observations", "B) The mode of the observations", "C) The number of observations", "D) The range of the observations"],
    ["A) Mode", "B) Mean", "C) Median", "D) Range"],
    ["A) The median interval", "B) The mean interval", "C) The modal interval", "D) The range interval"],
    ["A) Winsorized mean", "B) Mode", "C) Median", "D) Trimmed mean"],
    ["A) The mode", "B) The median", "C) The central tendency", "D) The range"],
    ["A) 10%", "B) 18%", "C) 20%", "D) 25%"],
    ["A) Variance", "B) Standard Deviation", "C) Mean Absolute Deviation (MAD)", "D) Range"],
    ["A) Mean Absolute Deviation (MAD)", "B) Range", "C) Coefficient of Variation (CV)", "D) Standard Deviation"],
    ["A) The amount of dispersion in a distribution relative to the distribution’s mean.", "B) The average of the absolute values of the deviations from the arithmetic mean.", "C) The positive square root of the variance.", "D) The difference between the largest and smallest values in a dataset."],
    ["A) Peaked around its mean.", "B) Symmetric about its mean.", "C) Not symmetric about its mean.", "D) Spread out from its mean."],
    ["A) Negative skewness.", "B) Zero skewness.", "C) Positive skewness.", "D) No skewness."],
    ["A) Mean > Mode > Median", "B) Mode > Median > Mean", "C) Median > Mean > Mode", "D) Mean > Median > Mode"],
    ["A) Symmetry of a distribution.", "B) Spread of a distribution.", "C) Peakedness of a distribution.", "D) Central tendency of a distribution."],
    ["A) Platykurtic.", "B) Mesokurtic.", "C) Leptokurtic.", "D) Symmetric."],
    ["A) Non-linear relationship between two random variables.", "B) Linear relationship between two random variables.", "C) Dispersion between two random variables.", "D) Central tendency of two random variables."],
    ["A) 0 to 1", "B) -1 to 0", "C) 0 to 100", "D) -1 to 1"],
    ["A) Perfect negative correlation.", "B) No linear relationship.", "C) Perfect positive correlation.", "D) Moderate positive correlation."],
    ["A) They tend to move in opposite directions.", "B) There is no relationship between X and Y.", "C) They tend to move together.", "D) The relationship between X and Y is unpredictable."],
    ["A) Covariance", "B) Variance", "C) Correlation coefficient", "D) Mean Absolute Deviation (MAD)"]

],
                "answers": [
    "B) Measures of Central Tendency",
    "C) The number of observations",
    "C) Median",
    "C) The modal interval",
    "D) Trimmed mean",
    "C) The central tendency",
    "B) 18%",
    "C) Mean Absolute Deviation (MAD)",
    "D) Standard Deviation",
    "A) The amount of dispersion in a distribution relative to the distribution’s mean.",
    "C) Not symmetric about its mean.",
    "C) Positive skewness.",
    "D) Mean > Median > Mode",
    "C) Peakedness of a distribution.",
    "C) Leptokurtic.",
    "B) Linear relationship between two random variables.",
    "D) -1 to 1",
    "C) Perfect positive correlation.",
    "C) They tend to move together.",
    "C) Correlation coefficient"

],
                "references": [
    "Page 42",
    "Page 42",
    "Page 42",
    "Page 43",
    "Page 43",
    "Page 44",
    "Page 44",
    "Page 45",
    "Page 46",
    "Page 47",
    "Page 56",
    "Page 56",
    "Page 56",
    "Page 56",
    "Page 50",
    "Page 53",
    "Page 53",
    "Page 53",
    "Page 53",
    "Page 53"
],
            },
            "Probability Trees and Conditional Expectations": {
                "questions": [
    "What is the primary use of a probability model?",
    "What is the purpose of a probability tree?",
    "What does the expected value of a random variable represent?",
    "How is the expected EPS calculated?",
    "What are conditional expected values contingent on?",
    "What will be the effect of a tariff on steel imports on the returns of a domestic steel producer’s stock?",
    "What is Bayes’ formula used for?",
    "If there is a 60% probability that the economy will outperform, what is the probability that a stock will go up?",
    "What is the probability that a stock will go down if the economy outperforms?",
    "Given that the stock has gains, what is the updated probability of an outperforming economy using Bayes’ formula?"
],
                "choices": [
    ["A) To make observations", "B) To look backward", "C) To describe past outcomes", "D) To describe the entire distribution of outcomes"],
    ["A) To show past outcomes", "B) To show the probabilities of various outcomes", "C) To calculate expected values", "D) To predict future events"],
    ["A) The least likely outcome", "B) The most frequent outcome", "C) The weighted average of the possible outcomes", "D) The median of the outcomes"],
    ["A) By multiplying the EPS with its probability", "B) By dividing the EPS by its probability", "C) By adding all the EPS values", "D) By taking the average of all EPS values"],
    ["A) Past events", "B) Future predictions", "C) The outcome of some other event", "D) Random occurrences"],
    ["A) No effect", "B) The stock’s conditional expected return will be lower", "C) The stock’s conditional expected return will be higher if the tariff is imposed", "D) The stock’s return will remain constant"],
    ["A) Calculating expected values", "B) Predicting future events", "C) Updating a given set of prior probabilities in response to new information", "D) Calculating variances"],
    ["A) 20%", "B) 30%", "C) 40%", "D) 70%"],
    ["A) 20%", "B) 30%", "C) 40%", "D) 50%"],
    ["A) 30%", "B) 42%", "C) 50%", "D) 60%"]

],
                "answers": [
                    "D", "B", "C", "A", "C", "C", "C", "D", "B", "C"
],
                "references": [
                    "Page 59", "Page 59", "Page 58", "Page 58", "Page 60", "Page 60", "Page 60", "Page 61", "Page 61", "Page 61"
],
            },
            "Portfolio Mathematics": {
                "questions": [
    "What is the formula to determine the expected return of a portfolio composed of n assets?",
    "How is the weight of Asset i determined in a portfolio?",
    "In finance, why are we often interested in how two random variables move in relation to each other?",
    "What does the covariance represent in the context of two assets' returns?",
    "How can the variance of a two-asset portfolio also be expressed?",
    "What is shortfall risk?",
    "How is the safety-first ratio for a portfolio determined?",
    "What does Roy’s safety-first criterion state?",
    "What is the primary objective of portfolio mathematics?",
    "How is the covariance between two assets' returns calculated given their joint probabilities?"

],
                "choices": [
                        ["A) Sum of weights multiplied by expected returns", "B) Sum of weights divided by expected returns", "C) Sum of expected returns divided by weights", "D) Weight of each asset multiplied by its variance"],
    ["A) Market value of the asset divided by market value of the portfolio", "B) Expected return of the asset divided by total expected return", "C) Variance of the asset divided by total variance", "D) Market value of the portfolio divided by market value of the asset"],
    ["A) To determine portfolio weight", "B) To calculate expected returns", "C) To assess investment risk", "D) To understand the correlation between assets"],
    ["A) The expected value of the product of the deviations of the two assets’ returns", "B) The correlation between the two assets", "C) The variance of the portfolio", "D) The expected return of the portfolio"],
    ["A) Using the correlation of the two assets’ returns", "B) Using the covariance of the two assets", "C) Using the weights of the two assets", "D) Using the expected returns of the two assets"],
    ["A) The probability that a portfolio’s value will exceed a specific value", "B) The risk associated with not diversifying a portfolio", "C) The probability that a portfolio’s value will fall below a specific value", "D) The risk associated with investing in high-risk assets"],
    ["A) Using the target return and standard deviation", "B) Using the expected return and variance", "C) Using the covariance and correlation", "D) Using the weights of the assets in the portfolio"],
    ["A) The optimal portfolio maximizes expected return", "B) The optimal portfolio minimizes variance", "C) The optimal portfolio maximizes safety-first ratio", "D) The optimal portfolio minimizes shortfall risk"],
    ["A) To maximize returns", "B) To minimize risk", "C) To calculate and interpret various measures related to portfolio returns", "D) To diversify investments"],
    ["A) By multiplying their expected returns", "B) By multiplying their variances", "C) Using a specific formula based on their joint probabilities", "D) By dividing their expected returns"]

                    
],
                "answers": [
                    "A", "A", "D", "A", "A", "C", "A", "D", "C", "C"
],
                "references": [
                    "Page 64", "Page 64", "Page 64", "Page 70", "Page 70", "Page 70", "Page 70", "Page 70", "Page 9", "Page 70"
],
            },
            "Simulation Methods": {
                "questions": [
    "What is the primary advantage of Monte Carlo simulation in terms of its inputs?",
    "What is a limitation of Monte Carlo simulation?",
    "What is the primary use of bootstrap resampling in simulations?",
    "In bootstrap resampling, how are repeated samples drawn?",
    "What is the main difference between Monte Carlo simulation and simulation using data from bootstrap resampling?",
    "What is Monte Carlo simulation primarily used for?",
    "In Monte Carlo simulation, how are values for risk factors generated?",
    "What is the main objective of using Monte Carlo simulation for valuing stock options?",
    "What is the primary limitation of simulation using bootstrap resampling?",
    "What is a key feature of bootstrap resampling?"

],
                "choices": [
    ["A) It is limited to the range of historical data.", "B) It can only test scenarios that have occurred in the past.", "C) Its inputs are not limited to the range of historical data.", "D) It is a simple method to use."],
    ["A) It is an analytic method.", "B) It provides answers that are always better than the assumptions used.", "C) It is fairly complex.", "D) It doesn't require any assumptions."],
    ["A) To generate data inputs based on observed data.", "B) To create new datasets.", "C) To test scenarios that have occurred in the past.", "D) To validate the results of other simulations."],
    ["A) Without replacement.", "B) Based on the population mean.", "C) With replacement.", "D) Based on the sample variance."],
    ["A) The complexity of the method.", "B) The source and scope of the data.", "C) The number of iterations required.", "D) The type of probability distributions used."],
    ["A) Only for valuing complex securities.", "B) Only for simulating profits/losses from a trading strategy.", "C) Only for calculating estimates of value at risk (VaR).", "D) For valuing complex securities, simulating profits/losses, and calculating VaR."],
    ["A) Deterministically.", "B) Based on historical data.", "C) Randomly based on assumed probability distributions.", "D) Based on future predictions."],
    ["A) To predict stock prices.", "B) To calculate the mean option value.", "C) To determine the best time to exercise the option.", "D) To assess the risk of the stock option."],
    ["A) It provides exact results.", "B) It can be used for any type of data.", "C) Its inputs are limited by the distribution of actual outcomes.", "D) It doesn't require any assumptions."],
    ["A) It doesn't use the observed sample.", "B) It draws subsamples without the same number of observations.", "C) It draws subsamples with the same number of observations.", "D) It doesn't allow sampled observations to be redrawn."]

],
                "answers": [
                    "C", "C", "A", "C", "B", "D", "C", "B", "C", "C"
],
                "references": [
                    "Page 73", "Page 73", "Page 74", "Page 74", "Page 74", "Page 73", "Page 73", "Page 73", "Page 74", "Page 74"
],
            },
            "Estimation and Inference": {
                "questions": [
    "What does probability sampling refer to?",
    "In random sampling, how is each item assumed to be selected?",
    "What is the main advantage of the bootstrap method over the jackknife?",
    "How can bootstrap resampling be described?",
    "What is a hypothesis?",
    "In the context of hypothesis testing, what does the population parameter refer to?",
    "What is the main objective of hypothesis testing procedures?",
    "What is the jackknife method primarily known for?",
    "How is the standard error of the sample mean estimated using the bootstrap method?",
    "What can the bootstrap method be used for, in addition to estimating the mean?"

],
                "choices": [
    ["A) Selecting a sample without knowing the probability of each sample member.",
     "B) Selecting a sample when we know the probability of each sample member in the overall population.",
     "C) Selecting a sample based on convenience.",
     "D) Selecting a sample based on judgment."],

    ["A) With varying probabilities.",
     "B) Based on historical data.",
     "C) Each item is assumed to have the same probability of being selected.",
     "D) Based on future predictions."],

    ["A) It is less computationally demanding.",
     "B) It can be used to construct confidence intervals for various statistics.",
     "C) It doesn't use the observed sample.",
     "D) It is less accurate."],

    ["A) Drawing samples without replacement.",
     "B) Drawing samples of varying sizes.",
     "C) Drawing repeated samples of size n from the full dataset, replacing the sampled observations each time.",
     "D) Drawing samples based on future predictions."],

    ["A) A statement about the value of a sample statistic.",
     "B) A statement about the value of a population parameter developed for the purpose of testing a theory or belief.",
     "C) A prediction about future events.",
     "D) A statement that cannot be tested."],

    ["A) The sample mean.",
     "B) The population variance.",
     "C) The population mean, m.",
     "D) The sample variance."],

    ["A) To make predictions about future events.",
     "B) To test a theory or belief based on sample statistics and probability theory.",
     "C) To determine the sample size.",
     "D) To calculate the population mean."],

    ["A) Being more computationally demanding than bootstrap.",
     "B) Being developed when computational power was not as readily available.",
     "C) Providing exact results.",
     "D) Being the most accurate resampling method."],

    ["A) By calculating the variance of the sample means.",
     "B) By calculating the standard deviation of these sample means.",
     "C) By using the observed sample only.",
     "D) By drawing samples without replacement."],

    ["A) Only for estimating the variance.",
     "B) For constructing confidence intervals for various statistics.",
     "C) Only for estimating the median.",
     "D) For predicting future outcomes."]

],
                "answers": [
                    "B", "C", "B", "C", "B", "C", "B", "B", "B", "B"
],
                "references": [
                    "Page 75", "Page 75", "Page 80", "Page 80", "Page 82", "Page 82", "Page 82", "Page 80", "Page 80", "Page 80"
],
            },
            "Hypothesis Testing": {
                "questions": [
    "What is the main purpose of hypothesis testing procedures?",
    "What is the null hypothesis designated as?",
    "Which hypothesis is concluded if there is sufficient evidence to reject the null hypothesis?",
    "What does the null hypothesis always include?",
    "What is a Type I error?",
    "What is the power of a test?",
    "What is the p-value for a hypothesis test?",
    "For a hypothesis concerning the value of a population variance, which test is used?",
    "To test a hypothesis concerning the equality of two population variances, which test is used?",
    "What is the decision for a hypothesis test based on?"
],
                "choices": [
    ["A) To predict future outcomes.", "B) To determine the sample size.", "C) To test a theory or belief based on sample statistics and probability theory.", "D) To calculate the population mean."],
    ["A) Ha", "B) H1", "C) H0", "D) H2"],
    ["A) Null hypothesis", "B) Alternative hypothesis", "C) Both null and alternative hypotheses", "D) Neither null nor alternative hypothesis"],
    ["A) The \"greater than\" condition.", "B) The \"less than\" condition.", "C) The \"equal to\" condition.", "D) The \"not equal to\" condition."],
    ["A) The rejection of the null hypothesis when it is actually true.", "B) The failure to reject the null hypothesis when it is actually false.", "C) The rejection of the alternative hypothesis when it is actually true.", "D) The failure to reject the alternative hypothesis when it is actually false."],
    ["A) The probability of rejecting the null when it is false.", "B) The probability of accepting the null when it is true.", "C) The probability of a Type I error.", "D) The probability of a Type II error."],
    ["A) The largest significance level for which the hypothesis would be accepted.", "B) The smallest significance level for which the hypothesis would be rejected.", "C) The average significance level.", "D) The median significance level."],
    ["A) t-test", "B) F-test", "C) χ^2 test", "D) z-test"],
    ["A) t-test", "B) F-test", "C) χ^2 test", "D) z-test"],
    ["A) The distribution of the sample.", "B) The distribution of the test statistic.", "C) The size of the sample.", "D) The significance level of the test."]
],
                "answers": [
                    "C", "C", "B", "C", "A", "A", "B", "C", "B", "B"
],
                "references": [
                    "Page 83", "Page 84", "Page 84", "Page 84", "Page 99", "Page 99", "Page 99", "Page 88", "Page 95", "Page 87"
],
            },
            "Parametric and Non-Parametric Tests of Independence": {
                "questions": [
    "What measures the strength of the relationship between two variables?",
    "If the correlation between two variables is zero, what does it indicate?",
    "Which test examines whether the ranks for multiple periods are correlated?",
    "What does a contingency table show?",
    "Which test statistic follows a t-distribution for sample sizes greater than 30 in a Spearman rank correlation test?",
    "What is the purpose of a runs test?",
    "What do parametric tests rely on?",
    "When is a nonparametric test called for?",
    "What does the null hypothesis always include in hypothesis testing procedures?",
    "What is the designation for the alternative hypothesis?"

],
                "choices": [
    ["A) Variance", "B) Standard deviation", "C) Correlation", "D) Mean"],
    ["A) There is a strong linear relationship.", "B) There is no linear relationship.", "C) The variables are inversely related.", "D) The variables are directly related."],
    ["A) Pearson correlation test", "B) Spearman rank correlation test", "C) Chi-square test", "D) F-test"],
    ["A) The correlation between two variables.", "B) The variance of a sample.", "C) The number of observations from a sample that have a combination of two characteristics.", "D) The standard deviation of two variables."],
    ["A) Pearson correlation coefficient", "B) Chi-square statistic", "C) F-statistic", "D) t-statistic"],
    ["A) To determine whether data are random.", "B) To test the mean of a sample.", "C) To determine the variance of a sample.", "D) To test the correlation between two variables."],
    ["A) Assumptions regarding the distribution of the population.", "B) The size of the sample.", "C) The correlation between two variables.", "D) The median of the sample."],
    ["A) When data are values rather than ranks.", "B) When the sample size is large.", "C) When the assumptions of parametric tests can't be supported.", "D) When the population is normally distributed."],
    ["A) The \"greater than\" condition.", "B) The \"less than\" condition.", "C) The \"equal to\" condition.", "D) The \"not equal to\" condition."],
    ["A) H0", "B) H1", "C) Ha", "D) H2"]
],
                "answers": [
                    "C", "B", "B", "C", "D", "A", "A", "C", "C", "C"
],
                "references": [
                    "Page 104", "Page 104", "Page 104", "Page 102", "Page 102", "Page 98", "Page 98", "Page 98", "Page 84", "Page 84"
],
            },
            "Simple Linear Regression": {
                "questions": [
    "What is the form of the linear equation often referred to as the line of best fit or regression line?",
    "What does the regression line minimize?",
    "What is another name for simple linear regression?",
    "What does the estimated intercept represent in a simple linear regression model?",
    "How is the estimated slope coefficient interpreted in a simple linear regression model?",
    "Which of the following is NOT an assumption made regarding simple linear regression?",
    "What does the total sum of squares (SST) measure?",
    "What does the sum of squared errors (SSE) measure?",
    "What is the coefficient of determination, \( R^2 \), in simple linear regression?",
    "In a simple linear regression, what does the F-test test for?"

],
                "choices": [
    ["A) \( Y = b_0 + b_1X \)", "B) \( Y = b_0X + b_1 \)", "C) \( Y = X + b_0 + b_1 \)", "D) \( Y = b_1 + b_0X \)"],
    ["A) Sum of squared errors (SSE)", "B) Sum of squared differences", "C) Sum of squared residuals", "D) All of the above"],
    ["A) Linear least squares regression", "B) Ordinary least squares regression", "C) Linear regression analysis", "D) Simple regression analysis"],
    ["A) The value of the dependent variable when the independent variable is zero.", "B) The slope of the regression line.", "C) The correlation between the dependent and independent variables.", "D) The variance of the residual term."],
    ["A) The change in the dependent variable for a one-unit change in the independent variable.", "B) The correlation between the dependent and independent variables.", "C) The variance of the residual term.", "D) The standard deviation of the independent variable."],
    ["A) A linear relationship exists between the dependent and the independent variable.", "B) The variance of the residual term is constant (homoskedasticity).", "C) The residual term is independently distributed (residuals are uncorrelated).", "D) The residual term follows a uniform distribution."],
    ["A) The total variation in the dependent variable.", "B) The variation in the dependent variable explained by the independent variable.", "C) The unexplained variation in the dependent variable.", "D) The correlation between the dependent and independent variables."],
    ["A) The total variation in the dependent variable.", "B) The variation in the dependent variable explained by the independent variable.", "C) The unexplained variation in the dependent variable.", "D) The correlation between the dependent and independent variables."],
    ["A) The proportion of the total variation of the dependent variable explained by the regression.", "B) The correlation between the dependent and independent variables.", "C) The variance of the residual term.", "D) The standard deviation of the dependent variable."],
    ["A) The significance of the intercept.", "B) The significance of the slope coefficient.", "C) The correlation between the dependent and independent variables.", "D) The variance of the residual term."]
],
                "answers": [
                    "A", "D", "B", "A", "A", "D", "A", "C", "A", "B"
],
                "references": [
                    "Page 107", "Page 107", "Page 107", "Page 122", "Page 122", "Page 122", "Page 122", "Page 122", "Page 122", "Page 122"
],
            },
            "Introduction to Big Data Techniques": {
                "questions": [
    "What does 'Capture' in the context of data processing methods refer to?",
    "Which term refers to the network of devices such as smartphones and smart buildings?",
    "What does 'Velocity' in the context of Big Data characteristics refer to?",
    "What is a challenge with machine learning results?",
    "Which term refers to the analysis of unstructured data in text or voice forms?",
    "What is 'Fintech' most accurately described as?",
    "Which technological development is most likely to be useful for analyzing Big Data?",
    "What does 'Curation' in the context of data processing methods refer to?",
    "What does the term 'fintech' refer to?",
    "What does the variety of data refer to in the context of Big Data characteristics?"
],
                "choices": [
    ["A) Archiving and accessing data.", "B) Adjusting for bad or missing data.", "C) Collecting data and transforming it into usable forms.", "D) Examining stored data to find needed information."],
    ["A) Big Data Network", "B) Internet of Data", "C) Internet of Things", "D) Data Web"],
    ["A) The volume of data.", "B) The variety of data structures.", "C) How quickly data are communicated.", "D) The quality of data."],
    ["A) They are always accurate.", "B) They can be a 'black box'.", "C) They are too simple.", "D) They are easily explainable."],
    ["A) Text analytics", "B) Voice recognition", "C) Data visualization", "D) Data curation"],
    ["A) The application of technology to the financial services industry.", "B) The replacement of government-issued money with electronic currencies.", "C) The clearing and settling of securities trades through distributed ledger technology.", "D) A type of cryptocurrency."],
    ["A) Machine learning.", "B) High-latency capture.", "C) The Internet of Things.", "D) Data visualization."],
    ["A) Archiving and accessing data.", "B) Assuring data quality by adjusting for bad or missing data.", "C) Collecting data and transforming it into usable forms.", "D) Examining stored data to find needed information."],
    ["A) A type of cryptocurrency.", "B) The application of technology to the financial services industry.", "C) A machine learning algorithm.", "D) A data visualization technique."],
    ["A) The volume of data.", "B) The varying degrees of structure in which data may exist.", "C) How quickly data are communicated.", "D) The quality of data."]
],
                "answers": [
                    "C", "C", "C", "B", "A", "B", "A", "B", "B", "B"
],
                "references": [
                    "Page 126", "Page 125", "Page 126", "Page 127", "Page 127", "Page 128", "Page 128", "Page 126", "Page 125", "Page 126"
],
            }
            
        },
        "ECONOMICS": {
            "Firms and Market Structures": {
                "questions":  [
    "Which of the following is a characteristic of all oligopoly markets?",
    "What does the Herfindahl-Hirschman Index measure?",
    "Which market structure is characterized by a single seller of a product with no good substitutes?",
    "In which market structure do firms compete less on price and more on marketing, perceived quality, and differences in features?",
    "Which of the following is NOT a characteristic of monopolistic competition?",
    "Which model is based on the assumption that competitors are unlikely to match a price increase by a firm in an oligopoly market?",
    "What does the term 'fintech' refer to?",
    "In which market structure do firms only need to pay attention to average market price, not the prices of individual competitors?",
    "Which of the following is a source of monopoly power?",
    "Which market structure is characterized by a large number of firms with relatively large market shares?"
],
                "choices": [
    ["A) No interdependence among firm pricing.", "B) High barriers to entry.", "C) Significant interdependence among firm pricing and output decisions.", "D) Perfect competition."],
    ["A) The number of firms in an industry.", "B) The degree of competition.", "C) The sum of the squared market shares of the largest N firms in an industry.", "D) The elasticity of firm demand."],
    ["A) Perfect competition.", "B) Oligopoly.", "C) Monopolistic competition.", "D) Monopoly."],
    ["A) Perfect competition.", "B) Monopolistic competition.", "C) Oligopoly.", "D) Monopoly."],
    ["A) Differentiated products.", "B) High barriers to entry.", "C) A large number of independent sellers.", "D) Firms face downward-sloping demand curves."],
    ["A) Kinked demand curve model.", "B) Cournot duopoly model.", "C) Nash equilibrium model.", "D) Stackelberg dominant firm model."],
    ["A) A type of cryptocurrency.", "B) The application of technology to the financial services industry.", "C) A machine learning algorithm.", "D) A data visualization technique."],
    ["A) Perfect competition.", "B) Monopolistic competition.", "C) Oligopoly.", "D) Monopoly."],
    ["A) High competition.", "B) Control over a resource specifically needed to produce the product.", "C) Low barriers to entry.", "D) Perfectly elastic demand."],
    ["A) Perfect competition.", "B) Monopolistic competition.", "C) Oligopoly.", "D) Monopoly."]
],
                "answers": ["C", "C", "D", "B", "B", "A", "B", "B", "B", "C"],
                "references": ["Page 144", "Page 148", "Page 137", "Page 137", "Page 137", "Page 139", "Page 125", "Page 137", "Page 137", "Page 139"],
            },           
            "Understanding Business Cycles": {
                "questions":  [
    "What is a key aspect of business cycles?",
    "What do credit cycles refer to?",
    "Which of the following can lead to 'bubbles' during economic expansions?",
    "Which of the following is a characteristic of an expansion in the business cycle?",
    "Which type of goods is highly cyclical in terms of consumer spending during business cycle phases?",
    "What is the significance of inventories as a business cycle indicator?",
    "Which of the following is NOT a category of economic indicators?",
    "During which phase of the business cycle does real GDP stop decreasing and begin increasing?",
    "What typically decreases during a contraction phase of the business cycle?",
    "Which economic sector would most likely correlate strongly and positively with credit cycles?"
],
                "choices": [
    ["A) They occur at regular intervals.", "B) They are always of the same duration.", "C) They recur, but not at regular intervals.", "D) They only apply to economies dominated by state planning."],
    ["A) Cyclical fluctuations in GDP.", "B) Cyclical fluctuations in employment rates.", "C) Cyclical fluctuations in interest rates and the availability of loans.", "D) Cyclical fluctuations in stock market prices."],
    ["A) Tight credit conditions.", "B) Stable interest rates.", "C) Loose credit conditions.", "D) High unemployment rates."],
    ["A) Decrease in consumer spending.", "B) Growth in most sectors of the economy.", "C) Decrease in business investment.", "D) High unemployment rates."],
    ["A) Non-durable goods.", "B) Services.", "C) Durable goods.", "D) Digital goods."],
    ["A) They indicate the profitability of firms.", "B) They show the overall economic growth.", "C) They are an important business cycle indicator.", "D) They represent the technological advancements in industries."],
    ["A) Leading indicators.", "B) Coincident indicators.", "C) Lagging indicators.", "D) Predictive indicators."],
    ["A) Expansion.", "B) Peak.", "C) Contraction.", "D) Trough."],
    ["A) Unemployment.", "B) Inflation pressure.", "C) Economic output.", "D) Both B and C."],
    ["A) Exports.", "B) Food retail.", "C) Construction.", "D) Manufacturing."]
],
                "answers": ["C", "C", "C", "B", "C", "C", "D", "D", "D", "C"],
                "references": ["Page 152", "Page 152", "Page 152", "Page 152", "Page 153", "Page 153", "Page 155", "Page 156", "Page 156", "Page 157"],
            },
            "Fiscal Policy": {
                "questions":  [
    "What are the objectives of fiscal policy?",
    "What is the belief of Keynesian economists regarding fiscal policy?",
    "What does discretionary fiscal policy refer to?",
    "Which of the following is NOT a delay that can limit the usefulness of fiscal policy changes?",
    "What is the significance of a current deficit in fiscal policies?",
    "What are the tools of fiscal policy?",
    "Which of the following is NOT a spending tool in fiscal policy?",
    "What is an advantage of fiscal policy?",
    "What is a disadvantage of fiscal policy tools?",
    "What is the belief of Monetarists regarding fiscal policy?"

],
                "choices": [
    ["A) Only to influence the level of economic activity.", "B) To redistribute wealth and income among segments of the population.", "C) To allocate resources among economic agents and sectors in the economy.", "D) All of the above."],
    ["A) It has no effect on economic growth.", "B) It can have a strong effect on economic growth when the economy is operating at less than full employment.", "C) It should be used to increase or decrease inflationary pressures over time.", "D) It should not be used to influence aggregate demand."],
    ["A) The spending and taxing decisions of a national government that are intended to stabilize the economy.", "B) Built-in fiscal devices triggered by the state of the economy.", "C) The effect of fiscal stimulus on the economy.", "D) The use of fiscal policy for social and political reasons."],
    ["A) Recognition lag.", "B) Action lag.", "C) Impact lag.", "D) Response lag."],
    ["A) It is always considered contractionary.", "B) It is always considered expansionary.", "C) It is judged relative to a structural (cyclically adjusted) deficit amount.", "D) It indicates the overall economic growth of a country."],
    ["A) Only spending tools.", "B) Only revenue tools.", "C) Both spending and revenue tools.", "D) Neither spending nor revenue tools."],
    ["A) Transfer payments.", "B) Current spending.", "C) Capital spending.", "D) Indirect taxation."],
    ["A) It can be used to quickly implement social policies via indirect taxes.", "B) It always leads to economic growth.", "C) It eliminates the need for monetary policy.", "D) It ensures a balanced budget."],
    ["A) They cannot be used for social policies.", "B) They always lead to inflation.", "C) Direct taxes and transfer payments take time to implement.", "D) They ensure economic stability."],
    ["A) They believe that fiscal policy should be used in an attempt to influence aggregate demand to counter cyclical movements in the economy.", "B) They believe that the effect of fiscal stimulus is only temporary.", "C) They believe that fiscal policy has a long-term impact on the economy.", "D) They believe that fiscal policy should be the primary tool for economic growth."]
],
                "answers": ["D", "B", "A", "D", "C", "C", "D", "A", "C", "B"],
                "references": [
    "Page 165",
    "Page 159",
    "Page 159",
    "Page 163",
    "Page 166",
    "Page 165",
    "Page 166",
    "Page 166",
    "Page 161",
    "Page 159"
],
            },
            "Monetary Policy": {
                "questions":  [
    "What is the primary objective of central banks?",
    "Which of the following is NOT a tool available to central banks for conducting monetary policy?",
    "What is the policy rate called in the United States?",
    "Which of the following actions is expansionary in nature?",
    "Which of the following is NOT part of the transmission mechanism for changes in the central bank’s policy rate?",
    "What do most central banks set as their target?",
    "What challenges do developing economies face in using monetary policy?",
    "Which of the following qualities is NOT associated with effective central banks?",
    "In the context of monetary policy, what does a liquidity trap refer to?",
    "Which of the following scenarios is most likely to result in a failure of monetary policy to achieve its objectives?"
],
                "choices": [
    ["A) Maintaining currency stability", "B) Controlling inflation", "C) Achieving full employment", "D) Ensuring positive sustainable economic growth"],
    ["A) Policy rate", "B) Reserve requirements", "C) Open market operations", "D) Currency pegging"],
    ["A) Refinancing rate", "B) Two-week repo rate", "C) Base rate", "D) Discount rate"],
    ["A) Increasing the policy rate", "B) Making open market sales of securities", "C) Decreasing reserve requirements", "D) Increasing reserve requirements"],
    ["A) Short-term bank lending rates", "B) Asset prices", "C) Expectations for future policy rate changes", "D) Corporate tax rates"],
    ["A) Interest rates", "B) Money supply", "C) Inflation rates", "D) Exchange rates"],
    ["A) Rapid financial innovation", "B) Lack of credibility of the monetary authority", "C) Undeveloped financial markets", "D) All of the above"],
    ["A) Independence", "B) Credibility", "C) Verifiability", "D) Transparency"],
    ["A) A situation where banks are unwilling to lend greater amounts", "B) A scenario where short-term rates cannot be reduced below zero", "C) A condition where monetary policy changes affect inflation expectations significantly", "D) A situation where individuals are willing to hold greater cash balances without a change in short-term rates"],
    ["A) Rapid economic growth", "B) Deflation", "C) Disinflation", "D) Hyperinflation"]
],
                "answers": [
    "B) Controlling inflation",
    "D) Currency pegging",
    "D) Discount rate",
    "C) Decreasing reserve requirements",
    "D) Corporate tax rates",
    "C) Inflation rates",
    "D) All of the above",
    "C) Verifiability",
    "D) A situation where individuals are willing to hold greater cash balances without a change in short-term rates",
    "B) Deflation"
],
                "references": [
    "\"Central banks have the objective of controlling inflation...\" Page: 176",
    "\"Policy tools available to central banks include the policy rate, reserve requirements, and open market operations.\" Page: 176",
    "\"The policy rate is called the discount rate in the United States...\" Page: 176",
    "\"Decreasing the policy rate, decreasing reserve requirements, and making open market purchases of securities are all expansionary.\" Page: 176",
    "\"The transmission mechanism for changes in the central bank’s policy rate through to prices and inflation includes one or more of the following: Short-term bank lending rates, Asset prices, Expectations for economic activity and future policy rate changes...\" Page: 176",
    "\"Most central banks set target inflation rates, typically 2%–3%, rather than targeting interest rates, as was once common.\" Page: 177",
    "\"Developing economies face unique challenges in using monetary policy due to undeveloped financial markets, rapid financial innovation, and lack of credibility of the monetary authority.\" Page: 177",
    "\"Effective central banks exhibit independence, credibility, and transparency.\" Page: 177",
    "\"Individuals may be willing to hold greater cash balances without a change in short-term rates (liquidity trap).\" Page: 177",
    "\"Monetary policy has a limited ability to act effectively against deflation because the policy rate cannot be reduced below zero, and demand for money may be highly elastic (liquidity trap).\" Page: 177"
],
            },
            "Introduction to Geopolitics": {
                "questions":  [
    "What does geopolitics refer to?",
    "Which of the following is a way to examine geopolitics?",
    "What does globalization refer to?",
    "Which of the following tools of geopolitics is described as a noncooperative economic tool?",
    "What is the primary concern of the World Trade Organization?",
    "Which of the following is NOT a tool of geopolitics?",
    "How does geopolitical risk affect investment values?",
    "Which of the following risks is often of high velocity?",
    "What is soft power?",
    "Which of the following best describes nationalism in the context of geopolitics and globalization?"

],
                "choices": [
    ["A. The study of geography and its impact on politics.", "B. Interactions among nations, including actions of state and nonstate actors.", "C. The study of political systems in different countries.", "D. The relationship between economic policies and political decisions."],
    ["A. Analysis of individual countries' GDP.", "B. Study of cultural differences among nations.", "C. Analysis of the extent to which individual countries cooperate with one another.", "D. Examination of political party systems in different countries."],
    ["A. Worldwide integration of economic activity and cultures.", "B. The spread of a single culture worldwide.", "C. The dominance of one country's economy over others.", "D. The political integration of nations."],
    ["A. Voluntary export restraints.", "B. Regional free trade agreements.", "C. Restrictions on conversion of currencies."],
    ["A. Providing economic assistance to developing countries.", "B. Ensuring that trade flows freely and works smoothly.", "C. Promoting international monetary cooperation."],
    ["A. Armed conflict.", "B. Espionage.", "C. Cultural exchange programs.", "D. Bilateral national security agreements."],
    ["A. By increasing or decreasing the risk premium investors require.", "B. By directly influencing the stock market indices.", "C. By changing the interest rates of a country.", "D. By influencing the GDP of a country."],
    ["A. Thematic risks.", "B. Exogenous risks.", "C. Event risks."],
    ["A. The ability to influence other countries using military force.", "B. The ability to influence other countries without using or threatening force.", "C. The economic dominance of one country over others.", "D. The political alliances formed between countries."],
    ["A. A nation pursuing its own economic interests in cooperation with other countries.", "B. A nation pursuing its own economic interests independently of, or in competition with, other countries.", "C. A nation's cultural dominance over others.", "D. A nation's political alignment with global powers."]
],
                "answers": [
    "B. Interactions among nations, including actions of state and nonstate actors.",
    "C. Analysis of the extent to which individual countries cooperate with one another.",
    "A. Worldwide integration of economic activity and cultures.",
    "A. Voluntary export restraints.",
    "B. Ensuring that trade flows freely and works smoothly.",
    "C. Cultural exchange programs.",
    "A. By increasing or decreasing the risk premium investors require.",
    "B. Exogenous risks.",
    "B. The ability to influence other countries without using or threatening force.",
    "B. A nation pursuing its own economic interests independently of, or in competition with, other countries."
],
                "references": [
    "Page 180: Geopolitics refers to interactions among nations, including the actions of state actors (national governments) and nonstate actors (corporations, nongovernment organizations, and individuals).",
    "Page 180: One way to examine geopolitics is through analysis of the extent to which individual countries cooperate with one another.",
    "Page 181: Globalization refers to the long-term trend toward worldwide integration of economic activity and cultures.",
    "Page 185: Examples of noncooperative economic tools include domestic content requirements, voluntary export restraints, and nationalization.",
    "Page 186: The World Trade Organization has the goal of ensuring that trade flows freely and works smoothly.",
    "Page 184: National security tools may include armed conflict, espionage, or bilateral or multilateral agreements designed to reinforce or prevent armed conflict.",
    "Page 184: Geopolitical risk affects investment values by increasing or decreasing the risk premium investors require to hold assets in a country or region.",
    "Page 184: To analyze the velocity of geopolitical risk, we can classify risks as high velocity (short term), medium velocity, or low velocity (long term). Exogenous risks often...",
    "Page 181: means through which a country may exercise soft power, which is the ability to influence other countries without using or threatening force.",
    "Page 181: We may contrast globalization with nationalism—which, in this context, refers to a nation pursuing its own economic interests independently of, or in competition with, the economic interests of other countries."
],
            },
            "International Trade": {
                "questions":  [
    "What is the primary benefit of international trade?",
    "Which of the following is a cited cost of free trade?",
    "What does a Free Trade Area primarily entail?",
    "In a Customs Union, what additional feature is present compared to a Free Trade Area?",
    "What is a primary characteristic of a Common Market?",
    "Which of the following is NOT a type of trading bloc or regional trading agreement (RTA)?",
    "What is the main function of the World Trade Organization (WTO)?",
    "Which of the following is a result of trade restrictions within each importing country?",
    "What is the primary effect of export subsidies?",
    "Which of the following is NOT a restriction on the flow of financial capital across borders?"

],
                "choices": [
    ["A) Increased domestic jobs in all sectors.", "B) Uniform prices for all goods and services.", "C) Increased variety of goods and reduced costs from specialization.", "D) Elimination of monopolies."],
    ["A) Decreased economic inequality.", "B) Loss of domestic jobs in an importing industry.", "C) Reduced variety of goods.", "D) Increased domestic production."],
    ["A) Common institutions and economic policy for the union.", "B) A single currency for all member countries.", "C) Removal of all barriers to import and export of goods and services among member countries.", "D) Common set of trade restrictions with nonmembers."],
    ["A) Removal of all barriers to the movement of labor and capital goods.", "B) Adoption of a common set of trade restrictions with nonmembers.", "C) Establishment of common institutions and economic policy.", "D) Adoption of a single currency."],
    ["A) Single currency adoption.", "B) Removal of barriers to the movement of labor and capital goods among member countries.", "C) Establishment of common institutions only.", "D) Restrictions on trade with nonmember countries."],
    ["A) Free Trade Area", "B) Economic Zone", "C) Customs Union", "D) Economic Union"],
    ["A) Providing financial assistance to developing countries.", "B) Ensuring that trade flows as smoothly, predictably, and freely as possible.", "C) Promoting international monetary cooperation.", "D) Facilitating the expansion and balanced growth of international trade."],
    ["A) Decrease in producer's surplus.", "B) Increase in consumer surplus.", "C) Increase in prices of imports and decrease in quantities of imports.", "D) Decrease in demand for domestically produced goods."],
    ["A) Increase export prices and benefit exporting countries.", "B) Decrease export prices and benefit importing countries.", "C) Increase tax revenue for the exporting country.", "D) Increase demand for domestically produced goods."],
    ["A) Prohibition of investment in the domestic country by foreigners.", "B) Prohibition of or taxes on the income earned on foreign investments by domestic citizens.", "C) Prohibition of foreign investments in certain domestic industries.", "D) Encouragement of repatriation of earnings of foreign entities operating in a country."]


],
                "answers": [
    "C) Increased variety of goods and reduced costs from specialization.",
    "B) Loss of domestic jobs in an importing industry.",
    "C) Removal of all barriers to import and export of goods and services among member countries.",
    "B) Adoption of a common set of trade restrictions with nonmembers.",
    "B) Removal of barriers to the movement of labor and capital goods among member countries.",
    "B) Economic Zone",
    "B) Ensuring that trade flows as smoothly, predictably, and freely as possible.",
    "C) Increase in prices of imports and decrease in quantities of imports.",
    "B) Decrease export prices and benefit importing countries.",
    "D) Encouragement of repatriation of earnings of foreign entities operating in a country."
],
                "references": [
    "Consider the global market for automobiles. Several countries export one type of autos and import other types. Consumers benefit from the greater variety offered, as well as the reduced costs from specialization. [Page: 188]",
    "While domestic consumers of imported goods and domestic producers of exported goods both gain, international trade imposes costs as well. The most cited costs of free trade are the loss of domestic jobs in an importing industry and increased economic inequality. [Page: 188]",
    "Free Trade Areas: All barriers to import and export of goods and services among member countries are removed. [Page: 192]",
    "Customs Union: All countries adopt a common set of trade restrictions with nonmembers. [Page: 192]",
    "Common Market: All barriers to the movement of labor and capital goods among member countries are removed. [Page: 192]",
    "Descriptions of Free Trade Areas, Customs Union, and Economic Union are provided. [Page: 192]",
    "The World Trade Organization (WTO) is the only international organization dealing with the global rules of trade between nations. Its main function is to ensure that trade flows as smoothly, predictably, and freely as possible. [Page: 183]",
    "Within each importing country, all of these restrictions will tend to do the following: Increase prices of imports and decrease quantities of imports. [Page: 194]",
    "Export subsidies decrease export prices and benefit importing countries at the expense of the government of the exporting country. [Page: 194]",
    "Restrictions on the flow of financial capital across borders include outright prohibition of investment in the domestic country by foreigners, prohibition of or taxes on the income earned on foreign investments by domestic citizens, prohibition of foreign investments in certain domestic industries, and restrictions on repatriation of earnings of foreign entities operating in a country. [Page: 194]"
],
            },
            "Capital Flows and the FX Market": {
                "questions":  [
    "What is the primary reason for capital flows between countries?",
    "Which of the following is a commonly cited objective of capital flow restrictions imposed by governments?",
    "What is the primary determinant of exchange rates in the short and intermediate term?",
    "Which of the following participants in the foreign exchange markets is referred to as hedgers?",
    "How is an exchange rate defined?",
    "What does a spot exchange rate refer to?",
    "Which of the following is NOT a participant in the foreign exchange market?",
    "What is the retail FX market primarily concerned with?",
    "How can a firm hedge its foreign exchange risk?",
    "What does a decrease in the USD/EUR exchange rate from 1.44 to 1.42 represent?"
],
                "choices": [
    ["A. Tourism and travel.", "B. Purchases of assets (both physical and financial) in one country by investors or governments in other countries.", "C. Cultural exchanges.", "D. Diplomatic relations."],
    ["A. Increase foreign investments.", "B. Reduce the volatility of domestic asset prices.", "C. Promote free trade.", "D. Encourage cultural exchanges."],
    ["A. Trade flows.", "B. Capital flows.", "C. Tourism.", "D. Diplomatic relations."],
    ["A. Those who enter into transactions that increase an existing foreign exchange risk.", "B. Those who speculate on currency values.", "C. Those who enter into transactions that decrease an existing foreign exchange risk.", "D. Those who only deal with domestic currencies."],
    ["A. The price or cost of units of one currency in terms of another.", "B. The interest rate difference between two countries.", "C. The trade balance between two countries.", "D. The GDP ratio of two countries."],
    ["A. The rate for future delivery.", "B. The rate for immediate delivery.", "C. The average rate over a year.", "D. The rate set by the central bank."],
    ["A. Large multinational banks.", "B. Corporations.", "C. Hedge fund managers.", "D. Local grocery stores."],
    ["A. FX transactions by large institutions.", "B. FX transactions by households and relatively small institutions.", "C. FX transactions by central banks.", "D. FX transactions by multinational corporations."],
    ["A. By speculating on currency values.", "B. By entering into a forward currency contract.", "C. By avoiding international transactions.", "D. By only dealing in domestic currencies."],
    ["A. Appreciation of the USD.", "B. Depreciation of the EUR.", "C. Appreciation of the EUR.", "D. Depreciation of the USD."]


],
                "answers": [
    "B. Purchases of assets (both physical and financial) in one country by investors or governments in other countries.",
    "B. Reduce the volatility of domestic asset prices.",
    "B. Capital flows.",
    "C. Those who enter into transactions that decrease an existing foreign exchange risk.",
    "A. The price or cost of units of one currency in terms of another.",
    "B. The rate for immediate delivery.",
    "D. Local grocery stores.",
    "B. FX transactions by households and relatively small institutions.",
    "B. By entering into a forward currency contract.",
    "B. Depreciation of the EUR."
],
                "references": [
    "Page 203: Capital flows result primarily from purchases of assets (both physical and financial) in one country by investors or governments in other countries.",
    "Page 204: Commonly cited objectives of capital flow restrictions include the following: Reduce the volatility of domestic asset prices.",
    "Page 204: Capital flows are the primary determinant of exchange rates in the short and intermediate term.",
    "Page 205: Participants in the foreign exchange markets are referred to as hedgers if they enter into transactions that decrease an existing foreign exchange risk.",
    "Page 198: An exchange rate is simply the price or cost of units of one currency in terms of another.",
    "Page 205: A spot exchange rate is the rate for immediate delivery.",
    "Page 205: The market for foreign exchange has various participants, including large multinational banks, corporations, investment fund managers, hedge fund managers, governments, and central banks.",
    "Page 198: The retail FX market refers to FX transactions by households and relatively small institutions.",
    "Page 197: By entering into a forward currency contract to sell 10 million euros in 90 days for a specific quantity of yen, the firm can reduce or eliminate the foreign exchange risk.",
    "Page 205: For a change in an exchange rate, we can calculate the percentage appreciation (price goes up) or depreciation (price goes down) of the base currency. For example, a decrease in the USD/EUR exchange rate from 1.44 to 1.42 represents a depreciation of the EUR relative to the USD of 1.39%."
],
            },
            "Exchange Rate Calculations": {
                "questions":  [
    "What is a spot exchange rate?",
    "What is a forward exchange rate?",
    "How can the percentage appreciation or depreciation of the base currency be calculated?",
    "How is an exchange rate defined?",
    "What does a forward quote in points indicate?",
    "How can a firm hedge its foreign exchange risk?",
    "How is the percentage change in the FX value of a currency calculated?",
    "What is the unit of points for a spot currency quote to four decimal places?",
    "How can the CHF/NZD cross rate be calculated using CHF/USD and NZD/USD rates?",
    "Which of the following is NOT a reason for capital flows between countries?"

],
                "choices": [
    ["A. The rate for future delivery.", "B. The rate for immediate delivery.", "C. The average rate over a year.", "D. The rate set by the central bank."],
    ["A. The rate for immediate delivery.", "B. The rate set by the central bank.", "C. The rate for future delivery.", "D. The average rate over a year."],
    ["A. By comparing the forward rate to the spot rate.", "B. By comparing the interest rates of two countries.", "C. By comparing the GDP of two countries.", "D. By comparing the trade balance of two countries."],
    ["A. The interest rate difference between two countries.", "B. The trade balance between two countries.", "C. The price or cost of units of one currency in terms of another.", "D. The GDP ratio of two countries."],
    ["A. The difference between the spot exchange rate and the forward exchange rate.", "B. The average rate over a year.", "C. The rate set by the central bank.", "D. The interest rate difference between two countries."],
    ["A. By speculating on currency values.", "B. By entering into a forward currency contract.", "C. By avoiding international transactions.", "D. By only dealing in domestic currencies."],
    ["A. By comparing the GDP of two countries.", "B. By comparing the trade balance of two countries.", "C. By comparing the forward rate to the spot rate.", "D. By comparing the interest rates of two countries."],
    ["A. 0.001", "B. 0.0001", "C. 0.01", "D. 0.1"],
    ["A. Multiplication of CHF/USD and NZD/USD.", "B. Division of CHF/USD by NZD/USD.", "C. Addition of CHF/USD and NZD/USD.", "D. Subtraction of CHF/USD from NZD/USD."],
    ["A. Tourism and travel.", "B. Cultural exchanges.", "C. Diplomatic relations.", "D. Purchases of assets in one country by investors in other countries."]
],
                "answers": [
    "B. The rate for immediate delivery.",
    "C. The rate for future delivery.",
    "A. By comparing the forward rate to the spot rate.",
    "C. The price or cost of units of one currency in terms of another.",
    "A. The difference between the spot exchange rate and the forward exchange rate.",
    "B. By entering into a forward currency contract.",
    "C. By comparing the forward rate to the spot rate.",
    "B. 0.0001",
    "B. Division of CHF/USD by NZD/USD.",
    "C. Diplomatic relations."
],
                "references": [
    "Page 200: A spot exchange rate is the currency exchange rate for immediate delivery, which for most currencies means the exchange of currencies takes place two days after the trade.",
    "Page 200: A forward exchange rate is a currency exchange rate for an exchange to be done in the future.",
    "Page 205: For a change in an exchange rate, we can calculate the percentage appreciation (price goes up) or depreciation (price goes down) of the base currency.",
    "Page 198: An exchange rate is simply the price or cost of units of one currency in terms of another.",
    "Page 210: A forward exchange rate quote typically differs from the spot quotation and is expressed in terms of the difference between the spot exchange rate and the forward exchange rate.",
    "Page 200: By entering into a forward agreement covering 10 million GBP at the 6-month forward rate of 1.192 EUR/GBP, the French firm has agreed to exchange 10 million GBP for 11.92 million euros in six months.",
    "Page 200: The percentage change in the dollar price of a euro is simply 1.39 / 1.42 − 1 = −0.0211 = −2.11%.",
    "Page 210: For a spot currency quote to four decimal places, such as 2.3481, each point is 0.0001, or 1/10,000th.",
    "Page 208: The CHF/NZD cross rate is (CHF/USD) / (NZD/USD) = 1.7799 / 2.2529 = 0.7900.",
    "(This is an inferred question based on the content provided.)"
],
            },
        # Topic PORTFOLIO MANAGEMENT from resing 12 to 19   
        },
        "PORTFOLIO MANAGEMENT (PART ONE)":{
            "Portfolio Risk and Return: Part I": {
    "questions": [
        "How is the relationship between portfolio risk and return for various portfolio allocations described?",
        "Which portfolio has the least risk on a risk versus return graph?",
        "What do risk-averse investors choose in terms of portfolios?",
        "Which asset class had the greatest average returns and greatest risk over the period 1926–2017?",
        "What is the result of combining a risk-free asset with a risky portfolio?",
        "What supports the two-fund separation theorem?",
        "What is the capital allocation line?",
        "Which portfolios make up the efficient frontier?",
        "What is the minimum-variance frontier?",
        "Which of the following is a characteristic of the returns of major investable asset classes?"
    ],
    "choices": [
        ["A. Exponential", "B. Linear", "C. Quadratic", "D. Logarithmic"],
        ["A. Optimal portfolio", "B. Maximum-variance portfolio", "C. Global minimum-variance portfolio", "D. Efficient portfolio"],
        ["A. Any portfolio on the minimum-variance frontier.", "B. Portfolios that lie on the efficient frontier.", "C. Portfolios with maximum risk.", "D. Portfolios with minimum return."],
        ["A. T-bills", "B. Large-capitalization stocks", "C. Small-capitalization stocks", "D. Bonds"],
        ["A. The relationship between portfolio risk and return becomes quadratic.", "B. The portfolio will have X% of the risk of the risky asset.", "C. The portfolio will have 100% of the risk of the risky asset.", "D. The portfolio risk becomes zero."],
        ["A. Combining two risky portfolios.", "B. Combining a risky portfolio with a risk-free asset.", "C. Combining two risk-free assets.", "D. Combining a risk-free asset with a bond."],
        ["A. The line representing the combination of two risky assets.", "B. The line representing the combination of two risk-free assets.", "C. The line representing possible combinations of risk-free assets and the optimal risky asset portfolio.", "D. The line representing the combination of bonds and stocks."],
        ["A. Portfolios with the least expected return for each level of risk.", "B. Portfolios with the greatest expected return for each level of risk.", "C. Portfolios with the least risk for each level of expected return.", "D. Portfolios with the maximum risk for each level of expected return."],
        ["A. A line formed by portfolios with the maximum variance.", "B. A line formed by portfolios with the least risk for each level of expected return.", "C. A line formed by portfolios with the greatest risk for each level of expected return.", "D. A line formed by portfolios with the maximum return for each level of risk."],
        ["A. Returns follow a normal distribution.", "B. Distributions are positively skewed.", "C. Distributions have greater kurtosis than a normal distribution.", "D. Returns are always positive."]
    ],
    "answers": [
        "B. Linear",
        "C. Global minimum-variance portfolio",
        "B. Portfolios that lie on the efficient frontier.",
        "C. Small-capitalization stocks",
        "B. The portfolio will have X% of the risk of the risky asset.",
        "B. Combining a risky portfolio with a risk-free asset.",
        "C. The line representing possible combinations of risk-free assets and the optimal risky asset portfolio.",
        "B. Portfolios with the greatest expected return for each level of risk.",
        "B. A line formed by portfolios with the least risk for each level of expected return.",
        "C. Distributions have greater kurtosis than a normal distribution."
    ],
    "references": [
        "Page 11: The relationship between portfolio risk and return for various portfolio allocations is linear, as illustrated in Figure 20.3.",
        "Page 22: On a risk versus return graph, the one risky portfolio that is farthest to the left (has the least risk) is known as the global minimum-variance portfolio.",
        "Page 22: Risk-averse investors would only choose a portfolio that lies on the efficient frontier.",
        "Page 9: Using U.S. data over the period 1926–2017 as an example, shown in Figure 20.1, small-capitalization stocks have had the greatest average returns and greatest risk over the period.",
        "Page 11: If we put X% of our portfolio into the risky asset, and the rest into the risk-free asset, our portfolio will have X% of the risk of the risky asset.",
        "Page 11: Combining a risky portfolio with a risk-free asset is the process that supports the two-fund separation theorem.",
        "Page 11: The line representing these possible combinations of risk-free assets and the optimal risky asset portfolio is referred to as the capital allocation line.",
        "Page 22: Those portfolios that have the greatest expected return for each level of risk make up the efficient frontier.",
        "Page 22: For each level of expected portfolio return, the portfolio that has the least risk is known as a minimum-variance portfolio. Taken together, these portfolios form a line called the minimum-variance frontier.",
        "Page 10: Distributions are negatively skewed, with greater kurtosis (fatter tails) than a normal distribution."
    ]
},
            "Portfolio Risk and Return: Part II": {
    "questions": [
        "What are the implications of combining a risk-free asset with a portfolio of risky assets?",
        "What does the capital allocation line (CAL) represent?",
        "What is systematic risk?",
        "Which type of risk can be diversified away?",
        "What is the capital market line (CML)?",
        "How can you increase the number of stocks in a portfolio?",
        "What is the M2 measure?",
        "What does the capital asset pricing model (CAPM) include?",
        "Which factor exposures can be included in a return generating model?",
        "What is the result of increasing the number of stocks in a portfolio?"
    ],
    "choices": [
        ["A. The portfolio becomes entirely risk-free.", "B. The portfolio's risk is reduced proportionally.", "C. The portfolio's risk is determined by the weight of the risky asset.", "D. The portfolio's return is maximized."],
        ["A. The combination of two risky assets.", "B. The combination of two risk-free assets.", "C. The possible combinations of risk-free assets and the optimal risky asset portfolio.", "D. The combination of bonds and stocks."],
        ["A. The risk associated with individual securities.", "B. The risk that can be diversified away.", "C. The risk associated with the overall market.", "D. The risk associated with specific industries."],
        ["A. Systematic risk.", "B. Market risk.", "C. Unsystematic risk.", "D. Total risk."],
        ["A. A line plotting return against total risk.", "B. A line plotting return against systematic risk.", "C. A line plotting return against unsystematic risk.", "D. A line plotting return against market risk."],
        ["A. By adding higher-beta stocks.", "B. By adding lower-beta stocks.", "C. By diversifying across industries.", "D. By diversifying across countries."],
        ["A. A risk-adjusted rate of return.", "B. A measure of total risk.", "C. A measure of market risk.", "D. A measure of unsystematic risk."],
        ["A. Only systematic risk.", "B. Only unsystematic risk.", "C. Both systematic and unsystematic risk.", "D. Neither systematic nor unsystematic risk."],
        ["A. Macroeconomic, fundamental, and statistical.", "B. Only macroeconomic.", "C. Only fundamental.", "D. Only statistical."],
        ["A. Unsystematic risk decreases.", "B. Systematic risk decreases.", "C. Total risk decreases.", "D. Market risk decreases."]
    ],
    "answers": [
        "C. The portfolio's risk is determined by the weight of the risky asset.",
        "C. The possible combinations of risk-free assets and the optimal risky asset portfolio.",
        "C. The risk associated with the overall market.",
        "C. Unsystematic risk.",
        "A. A line plotting return against total risk.",
        "A. By adding higher-beta stocks.",
        "A. A risk-adjusted rate of return.",
        "A. Only systematic risk.",
        "A. Macroeconomic, fundamental, and statistical.",
        "A. Unsystematic risk decreases."
    ],
    "references": [
        "Page 24: In the previous reading, we covered the mathematics of calculating the risk and return of a portfolio with a percentage weight of WA invested in a risky portfolio (P) and a weight of WB = 1 − WA invested in a risk-free asset.",
        "Page 24: The line representing these possible combinations of risk-free assets and the optimal risky asset portfolio is referred to as the capital allocation line.",
        "Page 26: Total risk equals systematic plus unsystematic risk. Market (systematic) risk is nondiversifiable risk.",
        "Page 26: Unique risk is diversifiable and is unsystematic.",
        "Page 45: The capital market line (CML) plots return against total risk, which is measured by standard deviation of returns.",
        "Page 45: When you increase the number of stocks in a portfolio, unsystematic risk will decrease at a decreasing rate. However, the portfolio's systematic risk can be increased by adding higher-beta stocks or decreased by adding lower-beta stocks.",
        "Page 41: The M2 measure produces the same risk-adjusted portfolio rankings as the Sharpe ratio, but is stated in percentage terms.",
        "(Inferred from the content provided.)",
        "Page 46: Macroeconomic, fundamental, and statistical factor exposures can be included in a return generating model to estimate the expected return of an investment.",
        "Page 45: When you increase the number of stocks in a portfolio, unsystematic risk will decrease at a decreasing rate."
    ]
}
        },
        "CORPORATE ISSUERS":{
            "Organizational Forms, Corporate Issuer Features, and Ownership": {
    "questions": [
        "What distinguishes a corporation from other business structures?",
        "Which of the following is a characteristic of a public corporation?",
        "What is a disadvantage faced by corporations in some countries?",
        "What is the nature of a sole proprietorship?",
        "In a sole proprietorship, how are profits taxed?",
        "Who is responsible for hiring the senior managers to operate a corporation?",
        "What is the liability of shareholders in a corporation?",
        "What is the legal status of a corporation?",
        "How can corporations raise large amounts of capital?",
        "What rights do shareholders have in a corporation?"
    ],
    "choices": [
        ["A. It is not a separate legal entity.", "B. All of its shareholders have unlimited liability.", "C. It is a legal entity separate from its owners.", "D. It cannot issue shares to the public."],
        ["A. It cannot trade shares on an organized market.", "B. It has an unlimited number of shareholders.", "C. It has shares that are sold to the public and traded on an organized market.", "D. It has no board of directors."],
        ["A. No taxation on profits.", "B. Double taxation of profits.", "C. No ability to distribute dividends.", "D. No legal rights."],
        ["A. It is a business owned and operated by multiple individuals.", "B. It is a business owned by an individual but operated by a separate entity.", "C. It is a business owned and operated by an individual.", "D. It is a business that cannot make profits."],
        ["A. As corporate income.", "B. As personal income of the owner.", "C. Not taxed at all.", "D. As dividends."],
        ["A. The shareholders directly.", "B. The board of directors.", "C. The CEO of the corporation.", "D. External consultants."],
        ["A. Unlimited liability.", "B. No liability.", "C. Limited to their investment.", "D. Limited to the corporation's total assets."],
        ["A. It is not a separate legal entity.", "B. It is an extension of its owners.", "C. It is a separate legal entity with many rights and responsibilities.", "D. It has no legal rights."],
        ["A. By borrowing from a single lender.", "B. By issuing bonds only.", "C. By issuing shares to the owners.", "D. By reinvesting all their profits."],
        ["A. No voting rights.", "B. Voting rights to elect the CEO.", "C. Voting rights to elect the board of directors.", "D. Voting rights to decide on daily operations."]
    ],
    "answers": [
        "C. It is a legal entity separate from its owners.",
        "C. It has shares that are sold to the public and traded on an organized market.",
        "B. Double taxation of profits.",
        "C. It is a business owned and operated by an individual.",
        "B. As personal income of the owner.",
        "B. The board of directors.",
        "C. Limited to their investment.",
        "C. It is a separate legal entity with many rights and responsibilities.",
        "C. By issuing shares to the owners.",
        "C. Voting rights to elect the board of directors."
    ],
    "references": [
        "Page 48: The feature that distinguishes a corporation, or limited company, from the other business structures is that a corporation is a legal entity separate from its owners and managers.",
        "Page 48: A public corporation (or a public limited company) is one that has shares that are sold to the public and trade in an organized market (stock exchange).",
        "Page 48: Depending on the country, a corporation's profits may be subject to double taxation if the government taxes companies on their earnings and it taxes dividends (which are distributions of earnings to owners) as personal income.",
        "Page 47: A sole proprietorship is a business owned and operated by an individual.",
        "Page 47: Profits are then taxed as personal income of the owner.",
        "Page 48: The board and the managers it hires are responsible for acting in the interests of the shareholders.",
        "Page 48: In this case, all of the corporation's shareholders have limited liability.",
        "Page 48: A corporation's legal identity is separate from that of its owners and is formed by filing an articles of incorporation with a regulatory body.",
        "Page 48: A corporation issues shares to the owners (shareholders), which allows it to raise large amounts of capital.",
        "Page 48: Shareholders have voting rights that allow them to elect the board of directors."
    ]
},
            "Investors and Other Stakeholders": {
    "questions": [
        "Who are considered the primary stakeholders of a corporation?",
        "What does stakeholder theory postulate?",
        "Which of the following is an environmental factor considered by investors?",
        "Which of the following is a social factor considered by investors?",
        "Which of the following is a corporate governance factor considered by investors?",
        "Who benefits from the upside of a company's growth when the company is financially sound?",
        "What is the primary focus of corporate governance under shareholder theory?",
        "Who has a residual interest in the corporation?",
        "Which group of stakeholders may have access to nonpublic information from company management?",
        "What is the primary concern of debtholders regarding a company?"
    ],
    "choices": [
        ["A. Only shareholders and debtholders.", "B. Shareholders, debtholders, and the board of directors.", "C. Shareholders, debtholders, board of directors, senior management, and employees.", "D. Shareholders, debtholders, board of directors, senior management, employees, creditors, suppliers, and government."],
        ["A. A company should prioritize shareholders over other stakeholders.", "B. A company should ignore the interests of stakeholders.", "C. A company needs to balance the interests of all stakeholders.", "D. A company should prioritize government interests."],
        ["A. Energy efficiency.", "B. Composition of the board.", "C. Waste management.", "D. Political contributions."],
        ["A. Air and water pollution.", "B. Customer satisfaction.", "C. Employee engagement.", "D. Waste management."],
        ["A. Energy efficiency.", "B. Customer satisfaction.", "C. Executive compensation.", "D. Waste management."],
        ["A. Equity holders.", "B. Debtholders.", "C. Both equity holders and debtholders.", "D. Neither equity holders nor debtholders."],
        ["A. Interests of the firm's employees.", "B. Interests of the firm's suppliers.", "C. Interests of the firm's shareholders.", "D. Interests of the firm's customers."],
        ["A. Lenders.", "B. Suppliers.", "C. Shareholders.", "D. Employees."],
        ["A. Public debtholders.", "B. Shareholders.", "C. Private debtholders.", "D. Employees."],
        ["A. The company's growth prospects.", "B. The company's ability to repay its obligations.", "C. The company's market value.", "D. The company's product quality."]
    ],
    "answers": [
        "D. Shareholders, debtholders, board of directors, senior management, employees, creditors, suppliers, and government.",
        "C. A company needs to balance the interests of all stakeholders.",
        "C. Waste management.",
        "C. Employee engagement.",
        "C. Executive compensation.",
        "A. Equity holders.",
        "C. Interests of the firm's shareholders.",
        "C. Shareholders.",
        "C. Private debtholders.",
        "B. The company's ability to repay its obligations."
    ],
    "references": [
        "Page 58: The primary stakeholders of a corporation include shareholders, debtholders, the board of directors, senior management, employees, creditors, suppliers, and government.",
        "Page 58: Stakeholder theory postulates that a company needs to balance the interests of all stakeholders.",
        "Page 58: Environmental factors include company contributions to climate change, air and water pollution, deforestation, energy efficiency, waste management, and water scarcity.",
        "Page 58: Social factors include the protection of customer privacy and information security, customer satisfaction, employee engagement, diversity and inclusion, labor relations, and community relations.",
        "Page 58: Corporate governance factors include the composition of the board, executive compensation, the internal audit function, bribery and corruption, political contributions, and lobbying.",
        "Page 59: If a company is financially sound, it is repaying interest and principal in full and on time. Debtholders have no additional claims to increased company profits. Equity holders benefit from the upside of a company's growth.",
        "Page 55: Under shareholder theory, the primary focus of corporate governance is the interests of the firm's shareholders, which is to maximize the market value of the firm's common equity.",
        "Page 55: Shareholders have a residual interest in the corporation, in that they have claim to the net assets of the corporation after all liabilities have been settled.",
        "Page 55: Private debtholders may have access to nonpublic information from company management, which decreases information asymmetry.",
        "Page 54: Debtholders are primarily concerned with a company's ability to repay its obligations and less concerned with its growth prospects."
    ]
},
            "Corporate Governance: Conflicts, Mechanisms, Risks, and Benefits": {
    "questions": [
        "What is the primary mechanism for shareholders to manage their relationships with companies?",
        "Which of the following is a primary mechanism for employees to manage relationships with employers?",
        "What does corporate governance refer to?",
        "Which of the following is a risk of poor governance?",
        "What can effective corporate governance improve?",
        "What is the principal-agent relationship?",
        "Which of the following is a conflict that can arise due to information asymmetry between shareholders and managers?",
        "Which committee is often required by regulations for firms?",
        "What is the objective of corporate governance?",
        "Which of the following is a benefit of effective corporate governance?"
    ],
    "choices": [
        ["A. Labor laws.", "B. Employment contracts.", "C. Proxy voting.", "D. Customer contracts."],
        ["A. Proxy voting.", "B. Labor laws.", "C. Customer contracts.", "D. Supplier contracts."],
        ["A. The external regulations governing a company.", "B. The system of internal controls and procedures of a company.", "C. The financial reporting standards of a company.", "D. The marketing strategies of a company."],
        ["A. Improved operational efficiency.", "B. Enhanced company reputation.", "C. Debt default.", "D. Increased firm value."],
        ["A. Risk of debt default.", "B. Operational efficiency.", "C. Legal risks.", "D. Reputational risks."],
        ["A. A relationship between two equal partners.", "B. A relationship between owners employing agents to act in their interests.", "C. A relationship between a company and its customers.", "D. A relationship between a company and its suppliers."],
        ["A. Managers may put in excessive effort.", "B. Managers may have less information about the firm's direction.", "C. Managers may put in insufficient effort.", "D. Managers may prioritize shareholder interests."],
        ["A. Compensation committee.", "B. Governance committee.", "C. Audit committee.", "D. Employee committee."],
        ["A. To maximize company profits.", "B. To manage and minimize conflicts of interest between stakeholders of the company.", "C. To prioritize shareholder interests.", "D. To ensure company monopoly in the market."],
        ["A. Increase in legal risks.", "B. Increase in operational inefficiencies.", "C. Reduction in the cost of debt.", "D. Increase in debt default risk."]
    ],
    "answers": [
        "C. Proxy voting.",
        "B. Labor laws.",
        "B. The system of internal controls and procedures of a company.",
        "C. Debt default.",
        "B. Operational efficiency.",
        "B. A relationship between owners employing agents to act in their interests.",
        "C. Managers may put in insufficient effort.",
        "C. Audit committee.",
        "B. To manage and minimize conflicts of interest between stakeholders of the company.",
        "C. Reduction in the cost of debt."
    ],
    "references": [
        "Page 66: Proxy voting is the primary shareholder mechanism.",
        "Page 64: Labor laws, employment contracts, and the right to form unions are the primary mechanisms for employees to manage relationships with employers.",
        "Page 62: Corporate governance is the system of internal controls and procedures by which individual companies are managed.",
        "Page 65: Failure to manage creditors' rights well can lead to debt default and bankruptcy.",
        "Page 65: Effective corporate governance can improve operational efficiency by ensuring that management and board member incentives align their interests well with those of the shareholders.",
        "Page 66: The principal-agent relationship refers to owners employing agents to act in their interests.",
        "Page 61: Managers may put in insufficient effort.",
        "Page 64: Regulations often require that firms have audit committees.",
        "Page 62: The objective is to manage and minimize conflicts of interest between stakeholders of the company.",
        "Page 67: Good corporate governance can improve operational efficiency and performance, reduce default risk, reduce the cost of debt, improve financial performance, and increase firm value."
    ]
},
            "Working Capital and Liquidity": {
    "questions": [
        "What does liquidity refer to for an asset?",
        "Which of the following is considered the least liquid current asset?",
        "What does the cash conversion cycle represent?",
        "Which of the following is a secondary liquidity source?",
        "What can an increase in the CCC indicate?",
        "Which of the following is a drag on liquidity?",
        "What is the primary objective of working capital management?",
        "Which approach to working capital management involves high levels of current assets financed with long-term debt and equity?",
        "Which of the following is a benefit of an aggressive approach to working capital management?",
        "What is the cash ratio formula?"
    ],
    "choices": [
        ["A. Its nearness to cash.", "B. Its nearness to settlement.", "C. Its market value.", "D. Its depreciation rate."],
        ["A. Marketable securities.", "B. Cash.", "C. Inventory.", "D. Accounts receivable."],
        ["A. The time it takes for a company to convert its investments into cash inflows.", "B. The time it takes for a company to pay off its debts.", "C. The time it takes for a company to generate profits.", "D. The time it takes for a company to process inventory."],
        ["A. Cash flow from operations.", "B. Cash saved by suspending dividends to shareholders.", "C. Marketable securities on hand.", "D. Bank borrowings."],
        ["A. Improved liquidity.", "B. Reduced liquidity.", "C. Increased profitability.", "D. Decreased operational efficiency."],
        ["A. Faster payments from customers.", "B. Excess inventory build-up.", "C. Faster payments to suppliers.", "D. Reduction in credit lines from banks."],
        ["A. To maximize firm profits.", "B. To ensure sufficient liquidity.", "C. To minimize operational costs.", "D. Both A and B."],
        ["A. Aggressive approach.", "B. Moderate approach.", "C. Conservative approach.", "D. Reactive approach."],
        ["A. Higher liquidity.", "B. Lower costs.", "C. Less financial risk.", "D. More flexibility during market disruptions."],
        ["A. (Cash + Marketable securities) / Total assets.", "B. (Cash + Marketable securities) / Current liabilities.", "C. Cash / Current liabilities.", "D. (Cash + Accounts receivable) / Current liabilities."]
    ],
    "answers": [
        "A. Its nearness to cash.",
        "C. Inventory.",
        "A. The time it takes for a company to convert its investments into cash inflows.",
        "B. Cash saved by suspending dividends to shareholders.",
        "B. Reduced liquidity.",
        "B. Excess inventory build-up.",
        "D. Both A and B.",
        "C. Conservative approach.",
        "B. Lower costs.",
        "B. (Cash + Marketable securities) / Current liabilities."
    ],
    "references": [
        "Page 70: For an asset, liquidity refers to its nearness to cash.",
        "Page 72: Because inventory is the least liquid current asset...",
        "Page 74: The cash conversion cycle (CCC) represents the time it takes for a company to convert its investments in inventory and other resources into cash inflows from sales.",
        "Page 70: Cash saved by suspending dividends to shareholders.",
        "Page 72: An increase in the CCC reduces an issuer's liquidity.",
        "Page 72: A drag on liquidity occurs when cash inflows lag. This can occur when excess inventory builds up...",
        "Page 73: Working capital management seeks to maximize firm profits while ensuring that sufficient liquidity is available to maintain the firm's operations and meet its obligations.",
        "Page 75: A conservative approach to working capital management involves high levels of current assets financed with long-term debt and equity.",
        "Page 73: The benefit of an aggressive approach is lower costs...",
        "Page 75: Cash ratio = (cash + marketable securities) / current liabilities."
    ]
},
            "Capital Investments and Capital Allocation": {
    "questions": [
        "What is the primary objective of the capital allocation process?",
        "Which step in the capital allocation process involves generating good project ideas?",
        "What is the Net Present Value (NPV)?",
        "Which of the following is NOT a principle of capital allocation?",
        "Which option allows a company to delay making an investment?",
        "What is the purpose of conducting a post-audit in the capital allocation process?",
        "Which of the following is a common mistake in the capital allocation process?",
        "Which option gives managers choices regarding the operational aspects of a project?",
        "What are the cash flows that change if the project is undertaken called?",
        "Which of the following is a benefit of the capital allocation process?",
        "Which option allows a company to make additional investments in a project if doing so creates value?",
        "Which step in the capital allocation process involves comparing the actual results to the projected results?",
        "Which of the following is NOT a real option relevant to capital investments?",
        "What is the discount rate used in NPV?",
        "Which of the following is a primary source for generating good project ideas in the capital allocation process?"
    ],
    "choices": [
        ["A. To generate good project ideas.", "B. To analyze project proposals.", "C. To maximize shareholder value.", "D. To monitor decisions and conduct post-audits."],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 4"],
        ["A. The sum of the present values of all expected incremental cash flows.", "B. The difference between the present value of cash inflows and outflows.", "C. The rate of return at which the NPV becomes zero.", "D. The sum of all future cash flows without discounting."],
        ["A. Decisions are based on after-tax cash flows.", "B. Firm value is based on accounting income.", "C. Incremental cash flows only.", "D. The timing of cash flows is important."],
        ["A. Timing options", "B. Abandonment options", "C. Expansion options", "D. Flexibility options"],
        ["A. To generate new project ideas.", "B. To analyze project proposals.", "C. To create the firm-wide capital budget.", "D. To identify systematic errors in the forecasting process."],
        ["A. Overly optimistic assumptions for pet projects.", "B. Basing decisions on after-tax cash flows.", "C. Properly accounting for inflation.", "D. Generating alternative investment ideas."],
        ["A. Timing options", "B. Abandonment options", "C. Expansion options", "D. Flexibility options"],
        ["A. Total cash flows", "B. Incremental cash flows", "C. Residual cash flows", "D. Nominal cash flows"],
        ["A. It determines the future success of the firm.", "B. It applies only to long-term assets.", "C. It is based on accounting income.", "D. It focuses solely on maximizing profits."],
        ["A. Timing options", "B. Abandonment options", "C. Expansion options", "D. Flexibility options"],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 4"],
        ["A. Timing options", "B. Abandonment options", "C. Expansion options", "D. Pricing options"],
        ["A. The firm's cost of equity", "B. The firm's cost of debt", "C. The firm's cost of capital, adjusted for the risk level of the project", "D. The market interest rate"],
        ["A. Competitors", "B. Senior management", "C. Market trends", "D. Customer feedback"]
    ],
    "answers": [
        "C. To maximize shareholder value.",
        "A. Step 1",
        "A. The sum of the present values of all expected incremental cash flows.",
        "B. Firm value is based on accounting income.",
        "A. Timing options",
        "D. To identify systematic errors in the forecasting process.",
        "A. Overly optimistic assumptions for pet projects.",
        "D. Flexibility options",
        "B. Incremental cash flows",
        "A. It determines the future success of the firm.",
        "C. Expansion options",
        "D. Step 4",
        "D. Pricing options",
        "C. The firm's cost of capital, adjusted for the risk level of the project",
        "B. Senior management"
    ],
    "references": [
        "Page 77: Finally, making good capital allocation decisions is consistent with management's primary goal of maximizing shareholder value.",
        "Page 77: Step 1: Idea generation.",
        "Page 77: Net present value (NPV) is the sum of the present values of all the expected incremental cash flows if a project is undertaken.",
        "Page 81: Decisions are based on after-tax cash flows, not accounting income.",
        "Page 85: Timing options allow a company to delay making an investment.",
        "Page 77: a post-audit should be used to identify systematic errors in the forecasting process and improve company operations.",
        "Page 82: Having overly optimistic assumptions for pet projects of senior management.",
        "Page 85: Flexibility options give managers choices regarding the operational aspects of a project.",
        "Page 82: Incremental cash flows are those that change if the project is undertaken.",
        "Page 77: the decisions made may determine the future success of the firm.",
        "Page 85: Expansion options allow a company to make additional investments in a project if doing so creates value.",
        "Page 77: Step 4: Monitoring decisions and conducting a post-audit.",
        "Page 85: The two main forms are price-setting and production-flexibility options.",
        "Page 77: The discount rate used is the firm's cost of capital, adjusted for the risk level of the project.",
        "Page 77: Ideas can come from a number of sources, including senior management..."
    ]
},
            "Capital Structure": {
    "questions": [
        "What is the primary objective of determining an optimal capital structure?",
        "Which theory of financial structure is based on information asymmetry?",
        "Which of the following is NOT an assumption of MM Proposition I?",
        "What does the static tradeoff theory seek to balance?",
        "Which of the following is a factor that affects a company's capacity to service debt?",
        "Which of the following is NOT a characteristic that influences the proportion of debt in a company's capital structure?",
        "What does MM Proposition I with no taxes or costs of financial distress suggest about a company's capital structure?",
        "What is the capital structure that a firm seeks to achieve on average over time to maximize firm value?",
        "Which of the following is the most preferred source of funds according to the pecking order theory?",
        "Which of the following is NOT a factor that determines a company's capacity to service debt?",
        "What is the result when the increase in the value of the tax shield from additional borrowing is exceeded by the value reduction of higher expected costs of financial distress?",
        "Which of the following is a benefit of using debt in the capital structure according to MM's propositions with taxes but without costs of financial distress?",
        "Which of the following is NOT an external factor that affects capital structures?",
        "Which of the following is NOT an assumption leading to MM Proposition I?",
        "Which theory suggests that the agency costs of equity are reduced by increased debt issuance?"
    ],
    "choices": [
        ["A. To minimize costs of financial distress.", "B. To maximize the use of equity.", "C. To maximize shareholder value.", "D. To minimize the use of debt."],
        ["A. Static Tradeoff Theory", "B. MM Proposition", "C. Pecking Order Theory", "D. Free Cash Flow Hypothesis"],
        ["A. Capital markets are perfectly competitive.", "B. There are no transactions costs, taxes, or bankruptcy costs.", "C. Investors have heterogeneous expectations.", "D. There is riskless borrowing and lending."],
        ["A. Costs of equity and debt.", "B. Costs of financial distress with tax shield benefits from using debt.", "C. Benefits of equity and debt.", "D. Costs of equity with benefits of debt."],
        ["A. Market trends.", "B. Competitor's capital structure.", "C. Industry norms.", "D. Customer feedback."],
        ["A. Growth and stability of revenue.", "B. Company's life cycle stage.", "C. Quality of company's products.", "D. Corporate tax rate."],
        ["A. It is irrelevant.", "B. It should be 100% equity.", "C. It should be 100% debt.", "D. It should be based on market conditions."],
        ["A. Optimal capital structure.", "B. Current capital structure.", "C. Target capital structure.", "D. Desired capital structure."],
        ["A. New equity.", "B. Debt financing.", "C. Retained earnings.", "D. External financing."],
        ["A. Characteristics of the business or industry.", "B. Company's existing debt level.", "C. Market trends.", "D. Corporate tax rate."],
        ["A. Optimal capital structure.", "B. Over-leveraged company.", "C. Under-leveraged company.", "D. Balanced capital structure."],
        ["A. Minimized WACC.", "B. Maximized company value.", "C. Balanced capital structure.", "D. Minimized company value."],
        ["A. Market conditions.", "B. Business cycle conditions.", "C. Corporate tax rate.", "D. Regulation."],
        ["A. There are no agency costs.", "B. Investment decisions are affected by financing decisions.", "C. Investors can borrow and lend at the risk-free rate.", "D. There are no transactions costs, taxes, or bankruptcy costs."],
        ["A. Static Tradeoff Theory", "B. MM Proposition", "C. Pecking Order Theory", "D. Free Cash Flow Hypothesis"]
    ],
    "answers": [
        "C. To maximize shareholder value.",
        "C. Pecking Order Theory",
        "C. Investors have heterogeneous expectations.",
        "B. Costs of financial distress with tax shield benefits from using debt.",
        "C. Industry norms.",
        "C. Quality of company's products.",
        "A. It is irrelevant.",
        "C. Target capital structure.",
        "C. Retained earnings.",
        "C. Market trends.",
        "A. Optimal capital structure.",
        "B. Maximized company value.",
        "C. Corporate tax rate.",
        "B. Investment decisions are affected by financing decisions.",
        "D. Free Cash Flow Hypothesis"
    ],
    "references": [
        "Page 97: determine an optimal capital structure based on the expected costs of financial distress.",
        "Page 98: Pecking order theory is based on information asymmetry.",
        "Page 90: Investors have homogeneous expectations.",
        "Page 93: The static tradeoff theory seeks to balance the costs of financial distress with the tax shield benefits from using debt.",
        "Page 88: External factors include market and business cycle conditions, regulation, and industry norms.",
        "Page 88: Company characteristics that influence the proportion of debt in a company's capital structure include the following: Growth and stability of revenue.",
        "Page 95: MM's propositions with no taxes or costs of financial distress are that a company's capital structure is irrelevant.",
        "Page 95: Target capital structure is the capital structure that a firm seeks to achieve on average over time to maximize firm value.",
        "Page 98: Pecking order theory... suggests that retained earnings are the first choice for financing an investment.",
        "Page 88: Internal factors include the characteristics of the business or industry, a company's life cycle stage, a company's existing debt level, and the corporate tax rate.",
        "Page 93: There is an amount of debt financing at which the increase in the value of the tax shield from additional borrowing is exceeded by the value reduction of higher expected costs of financial distress.",
        "Page 95: MM's propositions with taxes but without costs of financial distress are that a company's... value is maximized with 100% debt.",
        "Page 88: External factors include market and business cycle conditions, regulation, and industry norms.",
        "Page 90: Investment decisions are unaffected by financing decisions.",
        "Page 98: Under the free cash flow hypothesis, the agency costs of equity... are reduced by increased debt issuance."
    ]
},
            "Business Models": {
    "questions": [
        "What is the essence of a business model?",
        "Which of the following is NOT a conventional business model?",
        "What does a value proposition refer to?",
        "Which business model involves selling a piece of equipment for a relatively low price and making profits by selling a consumable used with the equipment?",
        "Which pricing strategy offers a product with basic functionality at no cost, but sells or unlocks other functionality for a fee?",
        "Which of the following business models benefits from user contributions such as content or traffic conditions?",
        "What do network effects refer to?",
        "Which of the following is an example of a two-sided or multi-sided network?",
        "Which business model involves a company producing products for others to market under their own brand name?",
        "In which business model does a company brand is used by another company on its products for a fee?",
        "Which of the following business models offers installation, service, support, or customization for complex equipment?",
        "Which of the following is NOT a part of a firm's channel strategy?",
        "Which of the following firms is considered a B2C firm?",
        "Which pricing strategy involves selling a product at low margins or even at a loss for a period of time to grow market share?",
        "Which of the following business models involves selling additional products after a purchase decision is made?"
    ],
    "choices": [
        ["A. How a firm will market its products.", "B. How a firm will provide its services, sell them, and make a profit.", "C. How a firm will structure its operations.", "D. How a firm will distribute its profits."],
        ["A. Natural resource producers.", "B. Software as a service (SaaS).", "C. Distributors.", "D. Retailers."],
        ["A. How a firm will market its products.", "B. How customers will value the characteristics of the product or service.", "C. The total value a firm brings to its shareholders.", "D. The value a firm places on its internal operations."],
        ["A. Freemium pricing.", "B. Penetration pricing.", "C. Razors-and-blades.", "D. Add-on pricing."],
        ["A. Penetration pricing.", "B. Freemium pricing.", "C. Subscription pricing.", "D. Add-on pricing."],
        ["A. Network effects.", "B. Licensing agreements.", "C. Crowdsourcing models.", "D. Value-added resellers."],
        ["A. The interconnectedness of a company's operations.", "B. The increase in the value of a network as its user base grows.", "C. The effects of a network outage on a company's operations.", "D. The effects of a company's network on its competitors."],
        ["A. WhatsApp.", "B. eBay.", "C. Waze.", "D. Airbnb."],
        ["A. Licensing agreements.", "B. Value-added resellers.", "C. Private label manufacturers or contract manufacturers.", "D. Subscription model."],
        ["A. Licensing agreements.", "B. Value-added resellers.", "C. Private label manufacturers.", "D. Subscription model."],
        ["A. Licensing agreements.", "B. Value-added resellers.", "C. Private label manufacturers.", "D. Subscription model."],
        ["A. How a firm will market its products.", "B. How a firm will sell directly to the buyers.", "C. How a firm will use intermediaries.", "D. How a firm will structure its operations."],
        ["A. A firm that sells machinery to other manufacturing companies.", "B. A firm that sells software solutions to other businesses.", "C. A firm that sells groceries to consumers.", "D. A firm that provides consulting services to other businesses."],
        ["A. Freemium pricing.", "B. Penetration pricing.", "C. Razors-and-blades.", "D. Add-on pricing."],
        ["A. Freemium pricing.", "B. Penetration pricing.", "C. Razors-and-blades.", "D. Add-on pricing."]
    ],
    "answers": [
        "B. How a firm will provide its services, sell them, and make a profit.",
        "B. Software as a service (SaaS).",
        "B. How customers will value the characteristics of the product or service.",
        "C. Razors-and-blades.",
        "B. Freemium pricing.",
        "C. Crowdsourcing models.",
        "B. The increase in the value of a network as its user base grows.",
        "D. Airbnb.",
        "C. Private label manufacturers or contract manufacturers.",
        "A. Licensing agreements.",
        "B. Value-added resellers.",
        "D. How a firm will structure its operations.",
        "C. A firm that sells groceries to consumers.",
        "B. Penetration pricing.",
        "D. Add-on pricing."
    ],
    "references": [
        "Page 100: “How we will provide it, sell it, and make a profit” is clearly an oversimplification, but this is the essence of a business model.",
        "Page 102: Conventional business models tend to be industry-specific. Examples include those followed by natural resource producers, manufacturers, distributors, retailers.",
        "Page 104: A value proposition refers to how a firm's customers will value the characteristics of the product or service.",
        "Page 101: Razors-and-blades. A company may find it profitable to sell a piece of equipment for a relatively low price (low margins) and make profits by selling a consumable used with the equipment.",
        "Page 101: Freemium pricing. Offer a product with basic functionality at no cost, but sell or unlock other functionality for a fee.",
        "Page 103: Crowdsourcing models benefit from user contributions'content in the case of Wikipedia, traffic conditions and events in the case of Waze.",
        "Page 103: Network effects refer to the increase in the value of a network as its user base grows.",
        "Page 103: Some networks are two-sided or multi-sided'such as Airbnb, which has a multitude of hosts and guests.",
        "Page 102: Private label manufacturers or contract manufacturers. Companies produce products for others to market under their own brand name.",
        "Page 102: Licensing agreements. A company brand is used by another company on its products for a fee.",
        "Page 102: Value-added resellers. They offer such things as installation, service, support, or customization for complex equipment.",
        "Page 100: A strategy that includes both digital and physical channels, such as internet sales with delivery at a physical location, is referred to as an omnichannel strategy.",
        "Page 100: Firms that sell to other businesses are said to be B2B (business to business) firms, while firms that sell to consumers are said to be B2C (business to consumer) firms.",
        "Page 101: Penetration pricing. A company offers a product at low margins or even at a loss for a period of time to grow market share.",
        "Page 101: Add-on pricing. Options or add-ons priced with high margins are added to the product after the purchase decision has been made."
    ]
}

        },
        "FINANCIAL STATEMENT ANALYSIS":{
            "Introduction to Financial Statement Analysis": {
    "questions": [
        "What is the first step in the financial statement analysis framework?",
        "Which step involves acquiring the company’s financial statements and other relevant data?",
        "What is the role of financial statement analysis?",
        "Which of the following is NOT a decision made using financial statement analysis?",
        "Where can an analyst find information about accounting estimates, assumptions, and methods chosen for reporting?",
        "If an auditor finds an exception to applicable accounting principles in a company's financial statements, she is most likely to issue a:",
        "Information about elections of members to a company’s board of directors is most likely found in:",
        "Which of the following steps in the financial statement analysis framework involves making appropriate adjustments to the financial statements?",
        "In which step of the financial statement analysis framework does an analyst decide what conclusions or recommendations the information supports?",
        "Which step in the financial statement analysis framework involves preparing a report and communicating it to its intended audience?"
    ],
    "choices": [
        ["A. Analyze and interpret the data.", "B. Report the conclusions or recommendations.", "C. State the objective and context.", "D. Gather data."],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 4"],
        ["A. To prepare financial statements.", "B. To use the information in a company’s financial statements to make economic decisions.", "C. To audit the company's financial records.", "D. To ensure compliance with tax regulations."],
        ["A. Whether to invest in the company’s securities.", "B. Assigning credit ratings to a company’s debt.", "C. Deciding the company's marketing strategy.", "D. Evaluating a company’s past performance."],
        ["A. The auditor’s opinion.", "B. Financial statement notes.", "C. Management discussion and analysis."],
        ["A. Dissenting opinion.", "B. Cautionary note.", "C. Qualified opinion."],
        ["A. A 10-Q filing.", "B. A proxy statement.", "C. Footnotes to the financial statements."],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 4"],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 4"],
        ["A. Step 4", "B. Step 5", "C. Step 6", "D. Step 7"]
    ],
    "answers": [
        "C. State the objective and context.",
        "B. Step 2",
        "B. To use the information in a company’s financial statements to make economic decisions.",
        "C. Deciding the company's marketing strategy.",
        "B. Financial statement notes.",
        "C. Qualified opinion.",
        "B. A proxy statement.",
        "C. Step 3",
        "D. Step 4",
        "B. Step 5"
    ],
    "references": [
        "Page 12: Step 1: State the objective and context.",
        "Page 12: Step 2: Gather data.",
        "Page 13: The role of financial statement analysis is to use the information in a company’s financial statements, along with other relevant information, to make economic decisions.",
        "Page 13: Examples of such decisions include whether to invest in the company’s securities or recommend them to investors, whether to extend trade or bank credit to the company, and assigning credit ratings to a company’s debt.",
        "Page 22: Information about accounting estimates, assumptions, and methods chosen for reporting is most likely found in financial statement notes.",
        "Page 20: If an auditor finds that a company’s financial statements have made a specific exception to applicable accounting principles, she is most likely to issue a qualified opinion.",
        "Page 20: Information about elections of members to a company’s board of directors is most likely found in a proxy statement.",
        "Page 12: Step 3: Process the data.",
        "Page 12: Step 4: Analyze and interpret the data.",
        "Page 12: Step 5: Report the conclusions or recommendations."
    ]
},
            "Analyzing Income Statements": {
    "questions": [
        "What does a vertical common-size income statement express each item as?",
        "Which profitability ratio is calculated as gross profit divided by revenue?",
        "Which of the following is the first step in revenue recognition?",
        "In which step of revenue recognition is revenue recognized when the performance obligations have been satisfied?",
        "Which of the following is NOT a method of analyzing revenue drivers?",
        "In a bottom-up analysis of revenue, which of the following is NOT a specific driver that revenue can be broken down into?",
        "Which of the following ratios can be quickly viewed within a common-size income statement?",
        "What can a firm do to increase its gross profit margin?",
        "Which ratio measures the profitability of a company as the ratio of net income to revenue?",
        "In the absence of any information indicating a change, an analyst may choose to incorporate which of the following from the prior period into a pro forma income statement for the next period?"
    ],
    "choices": [
        ["A. Percentage of assets.", "B. Percentage of revenue.", "C. Percentage of net income.", "D. Percentage of gross profit."],
        ["A. Operating profit margin.", "B. Net profit margin.", "C. Gross profit margin.", "D. EBITDA margin."],
        ["A. Determine a transaction price.", "B. Identify the contract or contracts with the customer.", "C. Recognize revenue when the performance obligations have been satisfied.", "D. Allocate the transaction price to the performance obligations."],
        ["A. Step 1", "B. Step 2", "C. Step 3", "D. Step 5"],
        ["A. Bottom-up analysis.", "B. Top-down analysis.", "C. Diagonal analysis.", "D. Segment analysis."],
        ["A. Price and volume.", "B. Business segments.", "C. Geography.", "D. Market share."],
        ["A. Current ratio.", "B. Debt-to-equity ratio.", "C. Gross profit margin.", "D. Quick ratio."],
        ["A. Decrease sales.", "B. Increase liabilities.", "C. Differentiate its products from the competition.", "D. Increase its debt ratio."],
        ["A. Gross profit margin.", "B. Operating profit margin.", "C. EBITDA margin.", "D. Net profit margin."],
        ["A. Gross profit.", "B. Operating profit margin.", "C. Net sales.", "D. EBITDA."]
    ],
    "answers": [
        "B. Percentage of revenue.",
        "C. Gross profit margin.",
        "B. Identify the contract or contracts with the customer.",
        "D. Step 5",
        "C. Diagonal analysis.",
        "D. Market share.",
        "C. Gross profit margin.",
        "C. Differentiate its products from the competition.",
        "D. Net profit margin.",
        "B. Operating profit margin."
    ],
    "references": [
        "Page 50: A vertical common-size income statement expresses each item as a percentage of revenue.",
        "Page 50: Two popular profitability ratios are gross profit margin (gross profit / revenue) and net profit margin (net income / revenue).",
        "Page 51: Step 1: Identify the contract or contracts with the customer.",
        "Page 51: Step 5: Recognize revenue when (or as) the performance obligations have been satisfied.",
        "Page 297: The focus is on revenue drivers, which can be analyzed on a bottom-up or top-down basis.",
        "Page 297: In a bottom-up analysis, revenue is broken down into specific drivers such as price and volume, business segments, or geography.",
        "Page 193: For example, the gross profit margin, operating profit margin, and net profit margin are all clearly indicated within a common-size income statement.",
        "Page 48: A firm might be able to increase prices if its products can be differentiated from other firms’ products as a result of factors such as brand names, quality, technology, or patent protection.",
        "Page 48: Another popular margin ratio is net profit margin. Net profit margin is the ratio of net income to revenue.",
        "Page 215: In the absence of any information indicating a change, an analyst may choose to incorporate the operating profit margin from the prior period into a pro forma income statement for the next period."
    ]
},
            "Analyzing Balance Sheets": {
    "questions": [
        "A vertical common-size balance sheet expresses each category of the balance sheet as a percentage of:",
        "Which of the following is NOT a characteristic of financial liabilities that are not issued at face value?",
        "What results from temporary timing differences between a firm’s tax reporting and its financial reporting?",
        "Which of the following ratios are used to measure a firm’s liquidity and solvency?",
        "In a horizontal common-size balance sheet, which year's values are standardized to 1.0 by construction?",
        "Net income shown on the common-size income statement is equivalent to which of the following ratios?",
        "Which of the following assets are classified as available-for-sale?",
        "Which of the following is NOT a behavioral factor that may affect an analyst’s forecasts?",
        "Which of the following is NOT a step in constructing a pro forma cash flow statement?",
        "Which of the following is NOT a force based on Porter’s analysis for evaluating the competitive position of a company?"
    ],
    "choices": [
        ["A. assets.", "B. equity.", "C. revenue.", "D. total liabilities."],
        ["A. Reported at fair value.", "B. Move toward par value at maturity.", "C. Reported at amortized cost.", "D. Result from temporary timing differences."],
        ["A. Deferred tax assets.", "B. Deferred tax liabilities.", "C. Current tax assets.", "D. Current tax liabilities."],
        ["A. Gross profit margin.", "B. Net profit margin.", "C. Current ratio.", "D. EBITDA margin."],
        ["A. Most recent year.", "B. First year.", "C. Last year.", "D. Middle year."],
        ["A. Gross profit margin.", "B. Net profit margin.", "C. Current ratio.", "D. EBITDA margin."],
        ["A. Tangible assets.", "B. Intangible assets.", "C. Financial instruments.", "D. None of the above."],
        ["A. Overconfidence bias.", "B. Illusion of control bias.", "C. Conservatism bias or anchoring.", "D. Market share bias."],
        ["A. Estimate income tax expense and cash taxes.", "B. Model the balance sheet based on items that flow from the income statement.", "C. Use historical depreciation and capital expenditures to estimate future capital expenditures.", "D. Estimate future sales based on past trends."],
        ["A. Bargaining power of suppliers.", "B. Threat of new entrants.", "C. Threat of substitute products.", "D. Market share dominance."]
    ],
    "answers": [
        "A. assets.",
        "A. Reported at fair value.",
        "B. Deferred tax liabilities.",
        "C. Current ratio.",
        "B. First year.",
        "B. Net profit margin.",
        "C. Financial instruments.",
        "D. Market share bias.",
        "D. Estimate future sales based on past trends.",
        "D. Market share dominance."
    ],
    "references": [
        "Page 64: A vertical common-size balance sheet expresses each item of the balance sheet as a percentage of total assets.",
        "Page 64: Financial liabilities that are not issued at face value are reported at amortized cost.",
        "Page 64: Deferred tax liabilities result from temporary timing differences between a firm’s tax reporting and its financial reporting.",
        "Page 64: Balance sheet ratios, along with common-size analysis, can be used to evaluate a firm’s liquidity and solvency.",
        "Page 195: The divisor here is the first-year values, so they are all standardized to 1.0 by construction.",
        "Page 195: Net income is shown on the common-size income statement as net income or revenues, which is the net profit margin.",
        "Page 64: classified as available-for-sale.",
        "Page 226: Behavioral factors may affect analyst’s forecasts.",
        "Page 226: Use the completed pro forma income statement and balance sheet to construct a pro forma cash flow statement.",
        "Page 227: An analyst can evaluate the competitive position of a company based on Porter’s five forces."
    ]
},
            "Analyzing Statements of Cash Flows I": {
    "questions": [
        "The cash flow statement provides information beyond the income statement because the income statement is based on:",
        "Which of the following is NOT a purpose of the cash flow statement?",
        "Which of the following is a characteristic of the direct method of presenting a firm’s statement of cash flows?",
        "Which of the following is a common component that appears on a statement of cash flows presented using the direct method?",
        "An increase in which of the following accounts is a use of cash?",
        "Which of the following is a source of cash?",
        "Which of the following activities typically relates to noncurrent assets?",
        "Which of the following is an advantage of the direct method of presenting CFO?",
        "Which of the following statements is true regarding earnings and the cash flow statement?",
        "The cash flow statement can be converted to common-size format by expressing each line item as a percentage of:"
    ],
    "choices": [
        ["A. Cash accounting.", "B. Accrual accounting.", "C. Direct accounting.", "D. Indirect accounting."],
        ["A. Understanding a company's cash receipts and payments.", "B. Evaluating a company's investing activities.", "C. Assessing a company's quality of earnings.", "D. Evaluating a company's market share."],
        ["A. Shows only accruals.", "B. Shows only cash payments and cash receipts.", "C. Shows only non-cash transactions.", "D. Shows only financing activities."],
        ["A. Cash collected from suppliers.", "B. Cash collected from customers.", "C. Cash used in financing activities.", "D. Cash used in investing activities."],
        ["A. Asset account.", "B. Equity account.", "C. Revenue account.", "D. Expense account."],
        ["A. Decrease in an asset account.", "B. Increase in an asset account.", "C. Decrease in a liability account.", "D. Increase in an expense account."],
        ["A. Operating activities.", "B. Investing activities.", "C. Financing activities.", "D. None of the above."],
        ["A. It presents the firm’s operating cash receipts and payments clearly.", "B. It is the only method allowed under IFRS.", "C. It is simpler to compute than the indirect method.", "D. It is the most commonly used method globally."],
        ["A. Earnings that significantly exceed operating cash flow may indicate aggressive accounting choices.", "B. Earnings that are lower than operating cash flow always indicate a company's poor performance.", "C. Earnings and operating cash flow are always equal.", "D. Earnings that are higher than operating cash flow indicate high-quality earnings."],
        ["A. Total assets.", "B. Total liabilities.", "C. Revenue.", "D. Equity."]
    ],
    "answers": [
        "B. Accrual accounting.",
        "D. Evaluating a company's market share.",
        "B. Shows only cash payments and cash receipts.",
        "B. Cash collected from customers.",
        "A. Asset account.",
        "A. Decrease in an asset account.",
        "B. Investing activities.",
        "A. It presents the firm’s operating cash receipts and payments clearly.",
        "A. Earnings that significantly exceed operating cash flow may indicate aggressive accounting choices.",
        "C. Revenue."
    ],
    "references": [
        "Page 66: The cash flow statement provides information for a reporting period beyond that available from the income statement, which is based on accrual, rather than cash, accounting.",
        "Page 66: Analysts use cash flow statements to understand: A company’s cash receipts and cash payments during an accounting period.",
        "Page 69: The direct method of presenting a firm’s statement of cash flows shows only cash payments and cash receipts over the period.",
        "Page 69: The following are common components that appear on a statement of cash flows presented using the direct method: Cash collected from customers.",
        "Page 68: An increase in an asset account is a use of cash.",
        "Page 68: a decrease in an asset account is a source of cash.",
        "Page 89: Investing activities typically relate to noncurrent assets.",
        "Page 89: The main advantage of the direct method is that it presents clearly the firm’s operating cash receipts and payments.",
        "Page 94: Earnings that significantly exceed operating cash flow may be an indication of aggressive (or even improper) accounting choices.",
        "Page 94: The cash flow statement can be converted to common-size format by expressing each line item as a percentage of revenue."
    ]
},
            "Analyzing Statements of Cash Flows II": {
    "questions": [
        "The cash flow statement provides information to assess the firm’s:",
        "Which of the following can be determined using the statement of cash flows?",
        "The cash flow statement can be converted to common-size format by expressing each line item as a percentage of:",
        "Earnings that significantly exceed operating cash flow may indicate:",
        "Which section of the cash flow statement reveals information about whether the firm is generating cash flow by issuing debt or equity?",
        "Which of the following methods presents the firm’s operating cash receipts and payments clearly?",
        "Operating activities typically relate to the firm’s:",
        "Investing activities typically relate to:",
        "Under which method of presenting CFO is net income adjusted for transactions that affect net income but do not affect operating cash flow?",
        "Which of the following is NOT a purpose of converting the cash flow statement to a common-size format?"
    ],
    "choices": [
        ["A. Market share.", "B. Competitive position.", "C. Liquidity, solvency, and financial flexibility.", "D. Product portfolio."],
        ["A. The company's market capitalization.", "B. Whether regular operations generate enough cash to sustain the business.", "C. The company's dividend yield.", "D. The company's price-to-earnings ratio."],
        ["A. Total assets.", "B. Total equity.", "C. Revenue.", "D. Total liabilities."],
        ["A. High-quality earnings.", "B. Aggressive accounting choices.", "C. Conservative accounting choices.", "D. Stable financial position."],
        ["A. Operating activities.", "B. Investing activities.", "C. Financing activities.", "D. Non-operating activities."],
        ["A. Accrual method.", "B. Direct method.", "C. Indirect method.", "D. Cash method."],
        ["A. Noncurrent assets.", "B. Noncurrent liabilities and equity.", "C. Current assets and current liabilities.", "D. Long-term investments."],
        ["A. Current assets and current liabilities.", "B. Noncurrent assets.", "C. Noncurrent liabilities and equity.", "D. Short-term investments."],
        ["A. Accrual method.", "B. Direct method.", "C. Indirect method.", "D. Cash method."],
        ["A. Identifying trends.", "B. Comparing with competitors.", "C. Assessing liquidity.", "D. Calculating the dividend yield."]
    ],
    "answers": [
        "C. Liquidity, solvency, and financial flexibility.",
        "B. Whether regular operations generate enough cash to sustain the business.",
        "C. Revenue.",
        "B. Aggressive accounting choices.",
        "C. Financing activities.",
        "B. Direct method.",
        "C. Current assets and current liabilities.",
        "B. Noncurrent assets.",
        "C. Indirect method.",
        "D. Calculating the dividend yield."
    ],
    "references": [
        "Page 92: The cash flow statement provides information to assess the firm’s liquidity, solvency, and financial flexibility.",
        "Page 92: An analyst can use the statement of cash flows to determine the following: Whether regular operations generate enough cash to sustain the business.",
        "Page 94: The cash flow statement can be converted to common-size format by expressing each line item as a percentage of revenue.",
        "Page 94: Earnings that significantly exceed operating cash flow may be an indication of aggressive (or even improper) accounting choices.",
        "Page 94: The financing activities section of the cash flow statement reveals information about whether the firm is generating cash flow by issuing debt or equity.",
        "Page 89: The main advantage of the direct method is that it presents clearly the firm’s operating cash receipts and payments.",
        "Page 89: Operating activities typically relate to the firm’s current assets and current liabilities.",
        "Page 89: Investing activities typically relate to noncurrent assets.",
        "Page 89: Under the indirect method of presenting CFO, net income is adjusted for transactions that affect net income but do not affect operating cash flow.",
        "Page 94: A revenue-based common-size cash flow statement is useful for identifying trends."
    ]
},
            "Analysis of Inventories": {
    "questions": [
        "Which of the following is NOT a required inventory disclosure under both U.S. GAAP and IFRS?",
        "Which of the following may indicate decreasing demand and potential future inventory write-downs?",
        "Under which accounting standard are reversals of inventory write-downs allowed?",
        "Which of the following may indicate that a firm expects an increase in demand?",
        "High inventory turnover, together with high sales growth relative to the industry average, suggests that:",
        "Which of the following is a potential indicator of slow-moving or obsolete inventory?",
        "What does a decline in gross profit margins coupled with positive sales growth suggest?",
        "Under IFRS, inventories are valued at the lower of:",
        "Which of the following is a sign of inadequate inventory quantities?",
        "Which of the following is NOT a potential source for further explanation regarding declining inventory balances?"
    ],
    "choices": [
        ["A. Cost flow method used.", "B. Total carrying value of inventory.", "C. Inventory turnover rate.", "D. Carrying value of inventories reported at fair value less selling costs."],
        ["A. Increase in raw materials.", "B. Increase in work in progress inventory.", "C. Finished goods inventory growing faster than sales.", "D. Increase in both raw materials and finished goods."],
        ["A. U.S. GAAP only.", "B. IFRS only.", "C. Both U.S. GAAP and IFRS.", "D. Neither U.S. GAAP nor IFRS."],
        ["A. Decrease in raw materials.", "B. Increase in finished goods inventory.", "C. Increase in raw materials or work in progress inventory.", "D. Decrease in both raw materials and finished goods."],
        ["A. The firm is facing supply-side shocks.", "B. The firm has obsolete inventory.", "C. High inventory turnover reflects greater efficiency.", "D. The firm is not managing its inventory effectively."],
        ["A. High inventory turnover.", "B. Low days of inventory on hand.", "C. Inventory turnover that is too low.", "D. High sales growth relative to the industry."],
        ["A. The company is facing decreasing demand.", "B. The cost of producing products has decreased.", "C. The company is facing supply-side shocks.", "D. The company has improved its efficiency."],
        ["A. Cost or market.", "B. Cost or net realizable value (NRV).", "C. Market or net realizable value (NRV).", "D. Replacement cost or net realizable value (NRV)."],
        ["A. High inventory turnover with slower growth.", "B. Low inventory turnover with high sales growth.", "C. High inventory turnover with high sales growth.", "D. Low inventory turnover with low sales growth."],
        ["A. Management discussion and analysis.", "B. Significant events disclosed in the accounts.", "C. Media and industry reports and journals.", "D. Company's marketing campaigns."]
    ],
    "answers": [
        "C. Inventory turnover rate.",
        "C. Finished goods inventory growing faster than sales.",
        "B. IFRS only.",
        "C. Increase in raw materials or work in progress inventory.",
        "C. High inventory turnover reflects greater efficiency.",
        "C. Inventory turnover that is too low.",
        "C. The company is facing supply-side shocks.",
        "B. Cost or net realizable value (NRV).",
        "A. High inventory turnover with slower growth.",
        "D. Company's marketing campaigns."
    ],
    "references": [
        "Page 109: Required inventory disclosures are similar under U.S. GAAP and IFRS and include the following: Cost flow method (LIFO, FIFO, etc.) used, Total carrying value of inventory, Carrying value of inventories reported at fair value less selling costs.",
        "Page 110: Finished goods inventory growing faster than sales may indicate declining demand and excessive or potentially obsolete inventory.",
        "Page 109: Reversals of inventory write-downs during the period, including a discussion of the circumstances of reversal (IFRS only because U.S. GAAP does not allow reversals).",
        "Page 110: For example, an increase in raw materials or work in progress inventory may indicate that the firm expects increase in demand.",
        "Page 116: High inventory turnover, together with high sales growth relative to the industry average, suggest that high inventory turnover reflects greater efficiency rather than inadequate inventory.",
        "Page 116: Inventory turnover that is too low (high days of inventory on hand) may be an indication of slow-moving or obsolete inventory.",
        "Page 113: Positive sales growth, coupled with declining margins, shows that the cost of producing disc golf products has increased.",
        "Page 114: Under IFRS, inventories are valued at the lower of cost or net realizable value (NRV).",
        "Page 110: High turnover with slower growth may be a sign of inadequate inventory quantities.",
        "Page 113: The analyst should seek out further explanation for the decline. Potential sources are as follows: Management discussion and analysis, Significant events disclosed in the accounts, Conferences and communication with the senior management,Media and industry reports and journals,The accounts of companies in the same industry"]
},
            "Analysis of Long-Term Assets": {
        "questions": [
            "Which of the following is NOT an intangible asset?",
            "Which of the following intangible assets are tested for impairment at least annually?",
            "Under IFRS, which of the following is NOT a requirement for an intangible asset to be identifiable?",
            "When is derecognition of a long-term asset typically done?",
            "What is the carrying value of a long-term asset equal to?",
            "Which of the following is a required disclosure for long-lived assets under both IFRS and U.S. GAAP?",
            "Which of the following is NOT a method to estimate the average age, economic life, and remaining useful life of a firm’s assets?",
            "Which of the following is NOT a characteristic of intangible assets?",
            "Which of the following is NOT a method used to recognize long-term assets?",
            "Which of the following is a sign of a less competitive firm regarding its assets?"
        ],
        "choices": [
            ["A. Patents", "B. Brand names", "C. Buildings", "D. Franchises"],
            ["A. Finite-lived assets", "B. Indefinite-lived assets", "C. Both finite and indefinite-lived assets", "D. Neither finite nor indefinite-lived assets"],
            ["A. It must be separable.", "B. It must be capable of being sold.", "C. It must arise from legal rights.", "D. It must have an indefinite life."],
            ["A. When assets are depreciated.", "B. When assets are sold, exchanged, or abandoned.", "C. When assets are revalued.", "D. When assets are impaired."],
            ["A. Original cost minus accumulated depreciation.", "B. Original cost plus accumulated depreciation.", "C. Original cost minus impairment charges.", "D. Original cost minus accumulated depreciation and any impairment charges."],
            ["A. Revaluation date.", "B. Carrying values for each class of asset.", "C. Carrying value using the historical cost model.", "D. Reversals of impairments."],
            ["A. Average Age", "B. Total Useful Life", "C. Remaining Useful Life", "D. Average Depreciation Rate"],
            ["A. They have physical substance.", "B. They lack physical substance.", "C. Some have finite lives.", "D. Some have indefinite lives."],
            ["A. Cost method", "B. Revaluation model", "C. Depreciation model", "D. Amortization model"],
            ["A. Newer, more efficient assets.", "B. Older, less-efficient assets.", "C. Assets with high salvage values.", "D. Assets with low accumulated depreciation."]
        ],
        "answers": [
            "C. Buildings",
            "B. Indefinite-lived assets",
            "D. It must have an indefinite life.",
            "B. When assets are sold, exchanged, or abandoned.",
            "D. Original cost minus accumulated depreciation and any impairment charges.",
            "B. Carrying values for each class of asset.",
            "D. Average Depreciation Rate",
            "A. They have physical substance.",
            "C. Depreciation model",
            "B. Older, less-efficient assets."
        ],
        "references": [
        "Page 119: Intangible assets are long-term assets that lack physical substance, such as patents, brand names, copyrights, and franchises.",
        "Page 119: Indefinite-lived intangible assets are not amortized, but they are tested for impairment at least annually.",
        "Page 119: Under IFRS, an identifiable intangible asset must be the following:",
        "Page 125: Derecognition occurs when assets are sold, exchanged, or abandoned.",
        "Page 125: The carrying value is equal to original cost minus accumulated depreciation and any impairment charges.",
        "Page 131: However, firms are generally required to disclose the following: Carrying values for each class of asset.",
        "Page 129: Three useful calculations (in years) for an analyst are as follows.",
        "Page 119: Intangible assets are long-term assets that lack physical substance.",
        "Page 119: Under U.S. GAAP, the cost method is required. IFRS allows companies to choose either the cost method or revaluation model for each class of asset.",
        "Page 129: Older, less-efficient assets may make a firm less competitive."
    ]
},
            "Topics in Long-Term Liabilities and Equity": {
    "questions": [
        "Which of the following is NOT a method of raising capital?",
        "What does a long position in an asset represent?",
        "Which of the following is a disadvantage of performance share units for a company?",
        "What is the objective of lease disclosures?",
        "How are lease liabilities and ROU assets treated for variable lease payments that depend on an index or rate?",
        "Which of the following is NOT included in the maturity analysis of lease liabilities?",
        "What does a short position in an asset represent?",
        "What is the leverage ratio?",
        "Which of the following is NOT a disadvantage of stock appreciation rights for a company?",
        "What is the main purpose of the cash flow statement?"
    ],
    "choices": [
    ["A. Borrowing", "B. Issuing equity", "C. Risk management", "D. Selling assets"],
    ["A. Future liability", "B. Current or future ownership", "C. Agreement to sell", "D. Borrowing an asset"],
    ["A. They result in new shares.", "B. They align employees’ and shareholders’ interest.", "C. They introduce bias toward risk-averse behavior.", "D. They result in cash outflows when the stock performs well."],
    ["A. To provide users with a basis to assess the effect of leasing activities.", "B. To highlight the profitability of the company.", "C. To showcase the company's assets.", "D. To provide details about the company's equity."],
    ["A. They are included in the lease liability and ROU asset.", "B. They are not included in the lease liability or ROU asset.", "C. They are only included in the ROU asset.", "D. They are only included in the lease liability."],
    ["A. Additions to ROU assets", "B. Split between current and long-term liabilities", "C. Next year's principal repayment", "D. Remaining principal repayments"],
    ["A. Current ownership", "B. Future ownership", "C. Agreement to sell or deliver an asset", "D. Agreement to buy an asset"],
    ["A. The value of the asset minus the value of the equity position.", "B. The value of the equity position divided by the value of the asset.", "C. The value of the asset divided by the value of the equity position.", "D. The value of the equity position minus the value of the asset."],
    ["A. They result in new shares.", "B. They align employees’ and shareholders’ interest.", "C. They introduce bias toward risk-averse behavior.", "D. They result in cash outflows when the stock performs well."],
    ["A. To determine the company's profitability.", "B. To assess the firm’s liquidity, solvency, and financial flexibility.", "C. To showcase the company's assets.", "D. To provide details about the company's equity."]
],
"answers": [
    "C. Risk management",
    "B. Current or future ownership",
    "D. They result in cash outflows when the stock performs well.",
    "A. To provide users with a basis to assess the effect of leasing activities.",
    "A. They are included in the lease liability and ROU asset.",
    "A. Additions to ROU assets",
    "C. Agreement to sell or deliver an asset",
    "B. The value of the asset divided by the value of the equity position.",
    "A. They result in new shares.",
    "B. To assess the firm’s liquidity, solvency, and financial flexibility."
],
    "references": [
        "[Page: 252]",
        "[Page: 252]",
        "[Page: 148]",
        "[Page: 149]",
        "[Page: 149]",
        "[Page: 149]",
        "[Page: 252]",
        "[Page: 252]",
        "[Page: 148]",
        "[Page: 92]"
    ]
}, 
            "Analysis of Income Taxes": {
    "questions": [
        "Which of the following items tend to be continuous in nature when analyzing trends in tax rates?",
        "What is taxable income?",
        "Which of the following is NOT a reason for differences between the statutory and effective tax rates?",
        "What is the tax expense also referred to as?",
        "What causes the firm’s effective tax rate to differ from the statutory tax rate?",
        "Which of the following is NOT disclosed in the footnotes regarding deferred tax information?",
        "What is the tax base?",
        "What is the main difference between financial accounting standards and income tax laws?",
        "Which of the following is a continuous item when analyzing a tax rate reconciliation?",
        "What is the effective tax rate typically expressed as a percentage of?"
    ],
"choices": [
    ["A. Different tax rates in different countries", "B. Large asset sales", "C. Tax holiday savings", "D. Termination dates for a tax holiday"],
    ["A. Income recognized in the income statement", "B. Income subject to tax based on the tax return", "C. Income after deducting tax expense", "D. Income before tax credits"],
    ["A. Different tax rates in various countries", "B. Tax-exempt income", "C. Temporary timing differences", "D. Nondeductible expenses"],
    ["A. Tax payable", "B. Tax provision", "C. Tax return", "D. Tax reconciliation"],
    ["A. Timing differences related to depreciation", "B. Permanent differences", "C. Changes in tax rates and legislation", "D. Tax holidays in some countries"],
    ["A. DTLs and DTAs", "B. Current-year tax effect of each type of temporary difference", "C. Tax expense for the current year", "D. Any unrecognized DTL for undistributed earnings of subsidiaries"],
    ["A. The net amount of an asset or liability used for tax reporting purposes", "B. The gross amount of an asset or liability used for financial reporting", "C. The amount of tax owed to the tax authorities", "D. The amount of tax expense recognized in the income statement"],
    ["A. They are identical in most countries", "B. Financial accounting standards are more lenient than tax laws", "C. The amount of income tax expense recognized in the income statement may differ from actual taxes owed", "D. Tax laws always result in higher tax expenses than financial accounting standards"],
    ["A. Tax holiday savings", "B. Termination dates for a tax holiday", "C. Different tax rates in different countries", "D. Large asset sales"],
    ["A. Gross profit", "B. Revenue", "C. Pretax income", "D. Net income"]
],

"answers": [
    "A. Different tax rates in different countries",
    "B. Income subject to tax based on the tax return",
    "C. Temporary timing differences",
    "B. Tax provision",
    "B. Permanent differences",
    "C. Tax expense for the current year",
    "A. The net amount of an asset or liability used for tax reporting purposes",
    "C. The amount of income tax expense recognized in the income statement may differ from actual taxes owed",
    "A. Different tax rates in different countries",
    "C. Pretax income"
],
    "references": [
        "[Page: 168]",
        "[Page: 157]",
        "[Page: 168]",
        "[Page: 161]",
        "[Page: 161]",
        "[Page: 173]",
        "[Page: 157]",
        "[Page: 157]",
        "[Page: 168]",
        "[Page: 48]"
    ]
},
            "Financial Analysis Techniques": {
    "questions": [
        "What are ratios useful for in financial analysis?",
        "Which of the following is NOT a limitation of ratio analysis?",
        "What does vertical common-size data represent for income statements?",
        "Which graphical representation shows changes in items from year to year?",
        "What is the purpose of sensitivity analysis in financial outcomes?",
        "In the DuPont analysis of return on equity, what is decomposed into its components?",
        "Which of the following is NOT a behavioral factor that may affect an analyst's forecasts?",
        "What is the main objective of the financial statement analysis framework?",
        "In financial analysis, what does horizontal common-size data present each item as?",
        "What can ratio analysis, in conjunction with other techniques, be used for?"
    ],
    "choices": [
    ["A. Only for internal comparisons", "B. Only for comparisons across firms", "C. Identifying questions that need to be answered", "D. Directly answering questions"],
    ["A. Ratios are not useful when viewed in isolation", "B. Ratios require adjustments for different accounting treatments", "C. Ratios can be used for direct comparisons without context", "D. Ratios can be misleading if companies use different accounting methods"],
    ["A. Data as a percentage of sales", "B. Data as a percentage of total assets", "C. Data as a percentage of net income", "D. Data as a percentage of equity"],
    ["A. Line graph", "B. Pie chart", "C. Stacked column graph", "D. Scatter plot"],
    ["A. To determine the exact outcome for key variables", "B. To ask 'what if' questions about key variables", "C. To confirm the accuracy of financial statements", "D. To compare with industry competitors"],
    ["A. Net profit margin", "B. Gross profit margin", "C. Return on equity (ROE)", "D. Return on assets (ROA)"],
    ["A. Overconfidence bias", "B. Illusion of control bias", "C. Conservatism bias or anchoring", "D. Financial leverage bias"],
    ["A. To analyze debt issues and equity securities", "B. To determine the profitability of a company", "C. To compare with industry competitors", "D. To evaluate the solvency of a company"],
    ["A. A percentage of its value in a base year", "B. A percentage of sales", "C. A percentage of total assets", "D. A percentage of equity"],
    ["A. To adjust financial statements", "B. To construct pro forma financial statements", "C. To determine the exact outcome for key variables", "D. To evaluate the solvency of a company"]
],

"answers": [
    "C. Identifying questions that need to be answered",
    "C. Ratios can be used for direct comparisons without context",
    "A. Data as a percentage of sales",
    "C. Stacked column graph",
    "B. To ask 'what if' questions about key variables",
    "C. Return on equity (ROE)",
    "D. Financial leverage bias",
    "A. To analyze debt issues and equity securities",
    "A. A percentage of its value in a base year",
    "B. To construct pro forma financial statements"
],
    "references": [
        "[Page: 191]",
        "[Page: 216]",
        "[Page: 216]",
        "[Page: 195]",
        "[Page: 215]",
        "[Page: 191]",
        "[Page: 226]",
        "[Page: 12]",
        "[Page: 216]",
        "[Page: 216]"
    ]
},
            "Introduction to Financial Statement Modeling": {
    "questions": [
        "What does a sales-based pro forma company model consist of?",
        "Which of the following is NOT a step in creating a sales-based pro forma company model?",
        "Which behavioral bias involves having too much faith in one's own work?",
        "In the financial statement analysis framework, what is the first step?",
        "What is the primary advantage of forecasting drivers in financial statement modeling?",
        "Which of the following is NOT a behavioral factor that may affect an analyst's forecasts?",
        "What is the purpose of the financial statement analysis framework?",
        "What is the result of the overconfidence bias in analysts?",
        "In financial statement modeling, what is used to estimate future capital expenditures and net PP&E for the balance sheet?",
        "What is the primary focus of forecasts that are distributed to external users?"
    ],
"choices": [
    ["A. Projected future balance sheets only", "B. Projected future financial statements based on past revenues", "C. Projected future financial statements based on an analyst’s estimate of future revenues", "D. Historical financial statements"],
    ["A. Estimating future capital expenditures", "B. Modeling the balance sheet based on items from the income statement", "C. Using historical depreciation to estimate future net PP&E", "D. Adjusting for inflation rates"],
    ["A. Conservatism bias", "B. Overconfidence bias", "C. Illusion of control bias", "D. Confirmation bias"],
    ["A. Gather data", "B. Process the data", "C. State the objective and context", "D. Analyze/interpret the processed data"],
    ["A. Simplicity", "B. Explanatory value and forecast accuracy", "C. Consistency with historical data", "D. Predictability"],
    ["A. Overconfidence bias", "B. Illusion of control bias", "C. Conservatism bias or anchoring", "D. Financial leverage bias"],
    ["A. To analyze debt issues and equity securities", "B. To determine the profitability of a company", "C. To compare with industry competitors", "D. To evaluate the solvency of a company"],
    ["A. They overestimate their forecasting errors", "B. They have a wider confidence interval for their forecasts", "C. They underestimate their forecasting errors", "D. They rely too much on external data sources"],
    ["A. Historical depreciation and capital expenditures", "B. Historical net income and revenue growth", "C. Historical working capital accounts", "D. Historical equity and liabilities"],
    ["A. Detailed breakdown of all financial statement items", "B. Key metrics such as revenue and EPS", "C. Internal company strategies and future plans", "D. Historical financial data and trends"]
],

"answers": [
    "C. Projected future financial statements based on an analyst’s estimate of future revenues",
    "D. Adjusting for inflation rates",
    "B. Overconfidence bias",
    "C. State the objective and context",
    "B. Explanatory value and forecast accuracy",
    "D. Financial leverage bias",
    "A. To analyze debt issues and equity securities",
    "C. They underestimate their forecasting errors",
    "A. Historical depreciation and capital expenditures",
    "B. Key metrics such as revenue and EPS"
],
    "references": [
        "[Page: 218]",
        "[Page: 219]",
        "[Page: 220]",
        "[Page: 12]",
        "[Page: 318]",
        "[Page: 226]",
        "[Page: 12]",
        "[Page: 220]",
        "[Page: 219]",
        "[Page: 318]"
    ]
},
            "Financial Reporting Quality": {
    "questions": [
        "What is the primary criterion for judging financial reporting quality?",
        "Which of the following is NOT a characteristic of decision-useful financial reporting?",
        "What does the quality of reported earnings refer to?",
        "Which of the following is a potential warning sign of channel stuffing?",
        "What does biased accounting within GAAP include?",
        "What is the objective of audits?",
        "Which of the following is a condition that provides an opportunity for low-quality financial reporting?",
        "What is the primary concern in determining the quality of a company’s reported earnings?",
        "What is the primary objective of financial reporting quality?",
        "Which of the following is NOT a likely element of low-quality financial reporting?"
    ],
"choices": [
    ["A. Compliance with the company's internal policies.", "B. Adherence to generally accepted accounting principles (GAAP).", "C. The company's stock price.", "D. The opinion of the company's auditors."],
    ["A. Relevance.", "B. Faithful representation.", "C. Neutrality.", "D. Predictability."],
    ["A. The accuracy of the earnings report.", "B. The sustainability and level of a firm’s earnings.", "C. The company's stock price.", "D. The opinion of the company's auditors."],
    ["A. An unusual increase in the firm’s receivables turnover.", "B. A decrease in the firm’s days of sales outstanding.", "C. An unusual increase in the firm’s days of sales outstanding.", "D. A decrease in the firm’s number of days of payables."],
    ["A. Neutral and aggressive accounting.", "B. Conservative and aggressive accounting.", "C. Conservative and neutral accounting.", "D. Aggressive and fraudulent accounting."],
    ["A. To guarantee the absence of error or fraud.", "B. To provide reasonable assurance that financial statements are free from material errors.", "C. To ensure compliance with company policies.", "D. To predict future financial performance."],
    ["A. The company has strong internal controls.", "B. The board of directors provides strong oversight.", "C. The company has a high stock price.", "D. The company has weak internal controls."],
    ["A. The accuracy of the earnings report.", "B. The sustainability and level of the earnings.", "C. The company's stock price.", "D. The opinion of the company's auditors."],
    ["A. To ensure compliance with company policies.", "B. To provide a positive image of the company.", "C. To adhere to generally accepted accounting principles (GAAP) and be decision useful.", "D. To predict future financial performance."],
    ["A. The company has strong internal controls.", "B. The board of directors provides inadequate oversight.", "C. Applicable accounting standards provide a large range of acceptable accounting treatments.", "D. The company's stock price is high."]
],

"answers": [
    "B. Adherence to generally accepted accounting principles (GAAP).",
    "D. Predictability.",
    "B. The sustainability and level of a firm’s earnings.",
    "C. An unusual increase in the firm’s days of sales outstanding.",
    "B. Conservative and aggressive accounting.",
    "B. To provide reasonable assurance that financial statements are free from material errors.",
    "D. The company has weak internal controls.",
    "B. The sustainability and level of the earnings.",
    "C. To adhere to generally accepted accounting principles (GAAP) and be decision useful.",
    "A. The company has strong internal controls."
],
    "references": [
        "[Page: 176]",
        "[Page: 176]",
        "[Page: 187,188]",
        "[Page: 187,188]",
        "[Page: 188]",
        "[Page: 188,189]",
        "[Page: 180]",
        "[Page: 177]",
        "[Page: 187,188]",
        "[Page: 180]"
    ]
}           
        },        
        "EQUITY INVESTMENTS":{
            "Market Organization and Structure": {
    "questions": [
        "What are the three main functions of the financial system?",
        "In which type of market do trades occur at any time the market is open?",
        "What are the three main categories of securities markets?",
        "Which behavioral bias involves having too much faith in one's own work?",
        "What is the result of the overconfidence bias in analysts?",
        "In which market is the stock only traded at specific times?",
        "Which market structure is used in smaller markets and also to set opening prices on major exchanges?",
        "What is the primary focus of forecasts that are distributed to external users?",
        "Which of the following is NOT a behavioral factor that may affect an analyst's forecasts?",
        "Which market structure allows investors to trade with dealers?"
    ],
"choices": [
    ["A. To allow entities to save and borrow money, raise equity capital, and trade assets.", "B. To determine the returns that equate the total supply of savings with the total demand for borrowing.", "C. To allocate capital to its most efficient uses.", "D. All of the above."],
    ["A. Call market.", "B. Continuous market.", "C. Quote-driven market.", "D. Brokered market."],
    ["A. Quote-driven markets, order-driven markets, and brokered markets.", "B. Call markets, continuous markets, and brokered markets.", "C. Auction markets, dealer markets, and brokered markets.", "D. Primary markets, secondary markets, and tertiary markets."],
    ["A. Conservatism bias.", "B. Overconfidence bias.", "C. Illusion of control bias.", "D. Confirmation bias."],
    ["A. They overestimate their forecasting errors.", "B. They have a wider confidence interval for their forecasts.", "C. They underestimate their forecasting errors.", "D. They rely too much on external data sources."],
    ["A. Call market.", "B. Continuous market.", "C. Quote-driven market.", "D. Brokered market."],
    ["A. Call market.", "B. Continuous market.", "C. Quote-driven market.", "D. Brokered market."],
    ["A. Detailed breakdown of all financial statement items.", "B. Key metrics such as revenue and EPS.", "C. Internal company strategies and future plans.", "D. Historical financial data and trends."],
    ["A. Overconfidence bias.", "B. Illusion of control bias.", "C. Conservatism bias or anchoring.", "D. Financial leverage bias."],
    ["A. Call market.", "B. Continuous market.", "C. Quote-driven market.", "D. Brokered market."]
],

"answers": [
    "D. All of the above.",
    "B. Continuous market.",
    "A. Quote-driven markets, order-driven markets, and brokered markets.",
    "B. Overconfidence bias.",
    "C. They underestimate their forecasting errors.",
    "A. Call market.",
    "A. Call market.",
    "B. Key metrics such as revenue and EPS.",
    "D. Financial leverage bias.",
    "C. Quote-driven market."
],
    "references": [
        "[Page: 229]",
        "[Page: 247]",
        "[Page: 247]",
        "[Page: 220]",
        "[Page: 220]",
        "[Page: 247]",
        "[Page: 247]",
        "[Page: 318]",
        "[Page: 226]",
        "[Page: 247]"
    ]
},
            "Security Market Indexes": {
    "questions": [
        "What does a security market index represent?",
        "What does a price index use for the return calculation?",
        "Which index measures the returns for an industry sector?",
        "Which index is the arithmetic mean of the prices of the index securities?",
        "What is the primary challenge in creating commodity indexes?",
        "Which index is based on the performance of commodity futures contracts and not the actual commodities?",
        "What type of index includes appraisal indexes, repeat property sales indexes, and indexes of real estate investment trusts?",
        "Which index is likely to have an upward bias due to voluntary reporting of performance to index providers?",
        "What does a broad market index provide?",
        "Which index typically consists of indexes from markets in several countries?"
    ],
    "choices": [
    ["A. The performance of a specific stock.", "B. The performance of an asset class, security market, or segment of a market.", "C. The performance of a specific sector.", "D. The performance of a specific country's economy."],
    ["A. Only the prices of the constituent securities.", "B. Both the price of and the income from the index securities.", "C. Only the income from the index securities.", "D. Neither the price nor the income from the index securities."],
    ["A. Style index.", "B. Broad market index.", "C. Sector index.", "D. Multi-market index."],
    ["A. Price-weighted index.", "B. Value-weighted index.", "C. Equal-weighted index.", "D. Sector index."],
    ["A. The weighting method.", "B. The performance of commodity futures contracts.", "C. The actual commodities.", "D. The volatility of commodities."],
    ["A. Real estate index.", "B. Commodity index.", "C. Hedge fund index.", "D. Sector index."],
    ["A. Commodity index.", "B. Hedge fund index.", "C. Real estate index.", "D. Sector index."],
    ["A. Commodity index.", "B. Hedge fund index.", "C. Real estate index.", "D. Sector index."],
    ["A. A measure of a specific sector's performance.", "B. A measure of a market's overall performance containing more than 90% of the market's total value.", "C. A measure of a specific style's performance.", "D. A measure of a specific country's performance."],
    ["A. Broad market index.", "B. Sector index.", "C. Style index.", "D. Multi-market index."]
],

"answers": [
    "B. The performance of an asset class, security market, or segment of a market.",
    "A. Only the prices of the constituent securities.",
    "C. Sector index.",
    "A. Price-weighted index.",
    "A. The weighting method.",
    "B. Commodity index.",
    "C. Real estate index.",
    "B. Hedge fund index.",
    "B. A measure of a market's overall performance containing more than 90% of the market's total value.",
    "D. Multi-market index."
],
    "references": [
        "[Page: 269]",
        "[Page: 269]",
        "[Page: 264]",
        "[Page: 268]",
        "[Page: 271]",
        "[Page: 271]",
        "[Page: 271]",
        "[Page: 271]",
        "[Page: 264]",
        "[Page: 264]"
    ]
},
            "Market Efficiency": {
    "questions": [
        "What does an informationally efficient capital market represent?",
        "In terms of market efficiency, what does short selling promote?",
        "What does the weak form of the efficient markets hypothesis (EMH) state?",
        "What does the semi-strong form of the EMH state?",
        "If markets are weak-form efficient, what is the implication for technical analysis?",
        "Which of the following is considered evidence of irrational behavior in investors?",
        "What does investor overconfidence refer to?",
        "What are the objectives of market regulation?",
        "In a perfectly efficient market, what investment strategy should investors use?",
        "Which form of market efficiency is based on both public information and inside or private information?"
    ],
"choices": [
    ["A. A market where security prices are biased estimates of their values.", "B. A market where current security prices reflect all available information.", "C. A market where investors can always beat the market.", "D. A market where security prices are based on past performance only."],
    ["A. It leads to excess volatility, reducing market efficiency.", "B. It promotes market efficiency by preventing assets from becoming overvalued.", "C. It has little effect on market efficiency.", "D. It increases the risk of unlimited losses."],
    ["A. Security prices reflect all public and private information.", "B. Security prices reflect all past price and volume information.", "C. Security prices reflect all publicly available information.", "D. Security prices are based on future predictions."],
    ["A. Security prices reflect all past price and volume information.", "B. Security prices reflect all public and private information.", "C. Security prices reflect all publicly available information.", "D. Security prices are based on future predictions."],
    ["A. Technical analysis consistently results in abnormal profits.", "B. Technical analysis does not consistently result in abnormal profits.", "C. Technical analysis is always successful in emerging markets.", "D. Technical analysis is based on future predictions."],
    ["A. Loss aversion.", "B. Investor underconfidence.", "C. Risk-seeking behavior.", "D. Overestimation of market prices."],
    ["A. Investors tend to underestimate their abilities.", "B. Investors tend to overestimate their abilities to analyze security information.", "C. Investors always make rational decisions.", "D. Investors rely solely on market trends."],
    ["A. To promote insider trading.", "B. To prevent insiders from exploiting other investors.", "C. To discourage financial reporting.", "D. To increase the risks for market participants."],
    ["A. Active investment strategy.", "B. Passive investment strategy.", "C. Speculative strategy.", "D. High-risk strategy."],
    ["A. Weak-form.", "B. Semi-strong form.", "C. Strong form.", "D. None of the above."]
],

"answers": [
    "B. A market where current security prices reflect all available information.",
    "B. It promotes market efficiency by preventing assets from becoming overvalued.",
    "B. Security prices reflect all past price and volume information.",
    "C. Security prices reflect all publicly available information.",
    "B. Technical analysis does not consistently result in abnormal profits.",
    "A. Loss aversion.",
    "B. Investors tend to overestimate their abilities to analyze security information.",
    "B. To prevent insiders from exploiting other investors.",
    "B. Passive investment strategy.",
    "C. Strong form."
],
    "references": [
        "[Page: 272]",
        "[Page: 274]",
        "[Page: 281]",
        "[Page: 281]",
        "[Page: 276]",
        "[Page: 280]",
        "[Page: 280]",
        "[Page: 253]",
        "[Page: 272]",
        "[Page: 281]"
    ]
},
            "Overview of Equity Securities": {
    "questions": [
        "What do common shares represent?",
        "How do common stockholders exercise their governance over the corporation?",
        "What determines the dividend to be paid on common equity?",
        "How can shareholders vote if they are unable to attend the annual meeting?",
        "How might a firm have different classes of common stock?",
        "What is the difference between public equity and private equity?",
        "Which of the following is a characteristic of private equity compared to public equity?",
        "What constitutes the returns on equity investments?",
        "How significant have gains from dividends and their reinvestment been for equity investors' long-term returns?",
        "How does preferred stock compare in risk to common stock?"
    ],
"choices": [
    ["A. A fixed interest rate.", "B. A residual claim on firm assets after debtholders and preferred stockholders.", "C. A guaranteed dividend payment.", "D. A non-voting right in the corporation."],
    ["A. Through fixed dividend payments.", "B. Through residual claims.", "C. Through voting rights.", "D. Through fixed interest rates."],
    ["A. It is a fixed amount set by regulators.", "B. It is determined by the market demand.", "C. It is determined by the firm periodically.", "D. It is always equal to the firm's profits."],
    ["A. They cannot vote.", "B. They can vote online.", "C. They can vote by phone.", "D. They can vote by proxy."],
    ["A. Based on the amount of dividend.", "B. Based on the seniority of liquidation.", "C. Based on the duration of ownership.", "D. Based on the country of issuance."],
    ["A. Public equity is issued to institutional investors, while private equity is traded publicly.", "B. Public equity is traded on stock exchanges, while private equity is issued to institutional investors via private placements.", "C. Public equity has voting rights, while private equity does not.", "D. Public equity is always more valuable than private equity."],
    ["A. Private equity markets are larger than public markets.", "B. Private equity markets are smaller but are growing rapidly.", "C. Private equity always offers higher returns than public equity.", "D. Private equity is more liquid than public equity."],
    ["A. Only price changes.", "B. Only dividend payments.", "C. Price changes, dividend payments, and gains or losses from changes in exchange rates.", "D. Only gains or losses from changes in exchange rates."],
    ["A. They have been a minor part of returns.", "B. They have been the only source of returns.", "C. They have been an important part of returns.", "D. They have had no impact on long-term returns."],
    ["A. Preferred stock is riskier because it has variable dividends.", "B. Preferred stock is less risky because it pays a known, fixed dividend.", "C. Preferred stock and common stock have the same risk profile.", "D. Preferred stock is riskier because it has no voting rights."]
],

"answers": [
    "B. A residual claim on firm assets after debtholders and preferred stockholders.",
    "C. Through voting rights.",
    "C. It is determined by the firm periodically.",
    "D. They can vote by proxy.",
    "B. Based on the seniority of liquidation.",
    "B. Public equity is traded on stock exchanges, while private equity is issued to institutional investors via private placements.",
    "B. Private equity markets are smaller but are growing rapidly.",
    "C. Price changes, dividend payments, and gains or losses from changes in exchange rates.",
    "C. They have been an important part of returns.",
    "B. Preferred stock is less risky because it pays a known, fixed dividend."
],
    "references": [
        "[Page: 283]",
        "[Page: 283]",
        "[Page: 283]",
        "[Page: 283]",
        "[Page: 285]",
        "[Page: 285]",
        "[Page: 285]",
        "[Page: 288]",
        "[Page: 288]",
        "[Page: 293]"
    ]
},
            "Company Analysis: Past and Present": {
    "questions": [
        "How can companies be grouped for constructing indexes and performing investment attribution analysis?",
        "What is the significance of a company's market share trend over time?",
        "What is the Herfindahl-Hirschman Index (HHI) used for?",
        "What is the primary focus when analyzing a company's operating costs?",
        "Which of the following is a key item typically included in an initial company research report?",
        "What is the role of industry and competitive analysis?",
        "Why is industry analysis useful for analysts?",
        "What is a limitation of financial ratios?",
        "Which of the following is a key item typically included in a subsequent company research report?",
        "What is a business model concerned with?"
    ],
"choices": [
    ["A. By product or service only.", "B. By geography.", "C. By their profitability.", "D. By their market capitalization."],
    ["A. It determines the company's profitability.", "B. It indicates how the company's products are viewed by customers.", "C. It determines the company's dividend policy.", "D. It indicates the company's debt level."],
    ["A. Measuring a company's profitability.", "B. Measuring market concentration.", "C. Measuring a company's debt level.", "D. Measuring a company's dividend payout."],
    ["A. Costs incurred in generating current period revenue.", "B. Costs associated with long-term investments.", "C. Costs associated with financing activities.", "D. Costs associated with mergers and acquisitions."],
    ["A. Detailed financial projections for the next decade.", "B. Company description.", "C. Daily stock price movements.", "D. Detailed biographies of all employees."],
    ["A. To determine a company's dividend policy.", "B. To assess the CEO's performance.", "C. To determine an industry’s base rate of profitability and assess companies’ positions.", "D. To predict daily stock price movements."],
    ["A. It helps in predicting daily stock price movements.", "B. It assists in improving financial forecasts by examining industry drivers.", "C. It helps in determining the CEO's compensation.", "D. It assists in predicting global economic trends."],
    ["A. They are always accurate and reliable.", "B. They are only informative when compared to those of other firms or to the company’s historical performance.", "C. They can predict future stock prices.", "D. They are universally applicable across all industries."],
    ["A. Detailed financial projections for the next decade.", "B. Analysis of new information.", "C. Daily stock price movements.", "D. Detailed biographies of all employees."],
    ["A. Only the company's products and services.", "B. Only the company's sales channels.", "C. The company's products, customers, sales channels, pricing, and reliance on key suppliers.", "D. Only the company's profitability metrics."]
],

"answers": [
    "B. By geography.",
    "B. It indicates how the company's products are viewed by customers.",
    "B. Measuring market concentration.",
    "A. Costs incurred in generating current period revenue.",
    "B. Company description.",
    "C. To determine an industry’s base rate of profitability and assess companies’ positions.",
    "B. It assists in improving financial forecasts by examining industry drivers.",
    "B. They are only informative when compared to those of other firms or to the company’s historical performance.",
    "B. Analysis of new information.",
    "C. The company's products, customers, sales channels, pricing, and reliance on key suppliers."
],
    "references": [
        "[Page: 307]",
        "[Page: 309]",
        "[Page: 309]",
        "[Page: 299]",
        "[Page: 301]",
        "[Page: 304]",
        "[Page: 304]",
        "[Page: 192]",
        "[Page: 301]",
        "[Page: 301]"
    ]
},
            "Industry and Competitive Analysis": {
    "questions": [
        "What is the primary purpose of industry and competitive analysis?",
        "How many steps are involved in industry and competitive analysis?",
        "Which of the following is NOT a step in industry and competitive analysis?",
        "What does Porter's Five Forces framework determine?",
        "Which of the following is NOT one of Porter’s five forces?",
        "What does the PESTLE analysis consist of?",
        "What does industry concentration often get expressed numerically through?",
        "What is the significance of a company's competitive strategy?",
        "What is the primary focus of industry analysis?",
        "What is the primary role of industry and competitive analysis?"
    ],
"choices": [
    ["A. To predict daily stock price movements.", "B. To analyze what drives industry size, profits, and market share.", "C. To determine the CEO's compensation.", "D. To predict global economic trends."],
    ["A. Three", "B. Four", "C. Five", "D. Six"],
    ["A. Define the industry.", "B. Predict the stock price.", "C. Analyze the industry structure.", "D. Determine industry participants’ competitive strategies."],
    ["A. Company's dividend policy.", "B. Industry competition.", "C. Daily stock price movements.", "D. CEO's performance."],
    ["A. Threat of new entrants.", "B. Power of regulators.", "C. Power of suppliers.", "D. Rivalry among existing competitors."],
    ["A. Political, Economic, Social, Technological, Legal, and Environmental influences.", "B. Product, Economic, Strategy, Technology, Legal, and Environmental factors.", "C. Political, Economic, Sales, Technological, Legal, and Environmental factors.", "D. Product, Entry, Social, Technology, Legal, and Environmental influences."],
    ["A. Porter's Five Forces.", "B. PESTLE analysis.", "C. Herfindahl-Hirschman Index.", "D. SWOT analysis."],
    ["A. It determines the company's stock price.", "B. It is either intentional or unintentional.", "C. It predicts the company's future profitability.", "D. It is always planned and follows a strict pattern."],
    ["A. To predict daily stock price movements.", "B. To improve financial forecasts by examining industry drivers.", "C. To determine the CEO's compensation.", "D. To predict global economic trends."],
    ["A. To determine a company's dividend policy.", "B. To assess the CEO's performance.", "C. To determine an industry’s base rate of profitability and assess companies’ positions.", "D. To predict daily stock price movements."]
],

"answers": [
    "B. To analyze what drives industry size, profits, and market share.",
    "C. Five",
    "B. Predict the stock price.",
    "B. Industry competition.",
    "B. Power of regulators.",
    "A. Political, Economic, Social, Technological, Legal, and Environmental influences.",
    "C. Herfindahl-Hirschman Index.",
    "B. It is either intentional or unintentional.",
    "B. To improve financial forecasts by examining industry drivers.",
    "C. To determine an industry’s base rate of profitability and assess companies’ positions."
],
    "references": [
        "[Page: 304]",
        "[Page: 304]",
        "[Page: 304]",
        "[Page: 310]",
        "[Page: 316]",
        "[Page: 316]",
        "[Page: 316]",
        "[Page: 313]",
        "[Page: 304]",
        "[Page: 304]"
    ]
},
            "Company Analysis: Forecasting": {
    "questions": [
        "What is the primary use of financial statement forecasts?",
        "Which of the following is NOT a key forecast object?",
        "What is the primary advantage of forecasting drivers?",
        "Which of the following is a recommended approach to forecasting?",
        "What is a bottom-up approach to revenue forecasting?",
        "When is it best to base forecasts on information?",
        "What should an analyst avoid when making forecasting models?",
        "What is the significance of management guidance in forecasting?",
        "Which of the following is NOT a bottom-up driver for forecasting?",
        "How should COGS and gross margin typically be estimated?"
    ],
"choices": [
    ["A. To determine the CEO's compensation.", "B. For both valuation and investment recommendations.", "C. To predict daily stock price movements.", "D. To assess the company's historical performance."],
    ["A. Financial statement lines with clear drivers.", "B. Revenue and EPS.", "C. Number of stores operating.", "D. Daily stock price movements."],
    ["A. Predicting daily stock price movements.", "B. Explanatory value and forecast accuracy.", "C. Determining the CEO's compensation.", "D. Assessing the company's historical performance."],
    ["A. Base forecasts on historical results.", "B. Predict daily stock price movements.", "C. Determine the CEO's compensation.", "D. Assess the company's historical performance."],
    ["A. Basing forecasts on global economic trends.", "B. Starting with an individual company or its reportable segments.", "C. Predicting daily stock price movements.", "D. Assessing the company's historical performance."],
    ["A. When the information is outdated.", "B. When the information is readily available and reasonably frequent and recurring.", "C. When the information is confidential.", "D. When the information is based on rumors."],
    ["A. Using historical data.", "B. Making the model overly complex without significant improvement.", "C. Using management's guidance.", "D. Considering external factors."],
    ["A. It is always accurate and reliable.", "B. It is based on rumors and speculations.", "C. Managers of public companies often reveal their earnings and revenue targets.", "D. It is always based on historical performance."],
    ["A. Average selling prices and volumes.", "B. Product-line or segment revenues.", "C. Daily stock price movements.", "D. Capacity-based measures."],
    ["A. Based on the CEO's compensation.", "B. As a percentage of revenue.", "C. Based on daily stock price movements.", "D. Based on the company's historical performance."]
],

"answers": [
    "B. For both valuation and investment recommendations.",
    "D. Daily stock price movements.",
    "B. Explanatory value and forecast accuracy.",
    "A. Base forecasts on historical results.",
    "B. Starting with an individual company or its reportable segments.",
    "B. When the information is readily available and reasonably frequent and recurring.",
    "B. Making the model overly complex without significant improvement.",
    "C. Managers of public companies often reveal their earnings and revenue targets.",
    "C. Daily stock price movements.",
    "B. As a percentage of revenue."
],
    "references": [
        "[Page: 318]",
        "[Page: 318]",
        "[Page: 318]",
        "[Page: 320]",
        "[Page: 322]",
        "[Page: 320]",
        "[Page: 320]",
        "[Page: 321]",
        "[Page: 322]",
        "[Page: 323]"
    ]
},
            "Equity Valuation: Concepts and Basic Tools": {
    "questions": [
        "What is intrinsic value or fundamental value defined as?",
        "What do analysts assume when doing valuation analysis for stocks?",
        "Which of the following is a type of discounted cash flow model?",
        "What is the primary advantage of using price multiples based on fundamentals?",
        "What is a disadvantage of asset-based models?",
        "What is the primary advantage of discounted cash flow models?",
        "What is a disadvantage of using price multiples based on fundamentals?",
        "What is enterprise value?",
        "What is the primary purpose of equity valuation models?",
        "When is an asset-based model most appropriate?"
    ],
"choices": [
    ["A. The current market price of an asset.", "B. The value investors would place on the asset if they had full knowledge of the asset's characteristics.", "C. The historical value of an asset.", "D. The future predicted value of an asset."],
    ["A. All stocks are fairly priced.", "B. Some stocks' prices deviate significantly from their intrinsic values.", "C. Stocks' prices are always overvalued.", "D. Stocks' prices always match their intrinsic values."],
    ["A. Price to earnings (P/E) ratio.", "B. Dividend discount model.", "C. Enterprise value to EBITDA ratio.", "D. Price to sales ratio."],
    ["A. They are very sensitive to the inputs.", "B. They are based on theoretically sound valuation models.", "C. They are always accurate.", "D. They are based on historical data."],
    ["A. They provide floor values.", "B. They are always accurate.", "C. Market values are often difficult to obtain.", "D. They are based on future predictions."],
    ["A. They are always accurate.", "B. They are based on the fundamental concept of discounted present value.", "C. Their inputs are easy to estimate.", "D. They are not sensitive to input values."],
    ["A. They are not widely accepted in the analyst community.", "B. They are not based on theoretically sound valuation models.", "C. Price multiples based on fundamentals will be very sensitive to the inputs.", "D. They cannot be used in time series and cross-sectional comparisons."],
    ["A. The market value of all a firm’s outstanding securities.", "B. The market value of all a firm’s outstanding securities minus cash and short-term investments.", "C. The total assets of a firm.", "D. The total liabilities of a firm."],
    ["A. To predict daily stock price movements.", "B. To determine the CEO's compensation.", "C. To estimate the intrinsic values of stocks and compare them to the stocks’ market prices.", "D. To assess the company's historical performance."],
    ["A. When a firm's assets are largely intangible.", "B. When a firm has primarily tangible short-term assets or assets with ready market values.", "C. When a firm is expanding rapidly.", "D. When a firm's assets are difficult to value."]
],

"answers": [
    "B. The value investors would place on the asset if they had full knowledge of the asset's characteristics.",
    "B. Some stocks' prices deviate significantly from their intrinsic values.",
    "B. Dividend discount model.",
    "B. They are based on theoretically sound valuation models.",
    "C. Market values are often difficult to obtain.",
    "B. They are based on the fundamental concept of discounted present value.",
    "C. Price multiples based on fundamentals will be very sensitive to the inputs.",
    "B. The market value of all a firm’s outstanding securities minus cash and short-term investments.",
    "C. To estimate the intrinsic values of stocks and compare them to the stocks’ market prices.",
    "B. When a firm has primarily tangible short-term assets or assets with ready market values."
],
    "references": [
        "[Page: 330]",
        "[Page: 330]",
        "[Page: 330]",
        "[Page: 349]",
        "[Page: 349]",
        "[Page: 348]",
        "[Page: 349]",
        "[Page: 330]",
        "[Page: 330]",
        "[Page: 349]"
    ]
}
        },
        "FIXED INCOME":{
            "Fixed-Income Instrument Features": {
    "questions": [
        "What are major types of fixed-income instruments?",
        "What is the capital raised from bonds typically used for?",
        "Who are the major issuers of bonds?",
        "What is the maturity date of a bond?",
        "What are bonds backed by the cash flows from financial assets called?",
        "What is the typical form of interest on a bond?",
        "What is the term for bonds that pay periodic interest based on the prevailing market rate of interest at the time future coupon payments are made?",
        "What is the variable market rate of interest on an FRN called?",
        "What is the added margin on an FRN typically expressed in?",
        "What is a loan structure in which the periodic payments include both interest and some repayment of principal called?"
    ],
"choices": [
    ["A. Stocks and bonds.", "B. Loans and equities.", "C. Loans and bonds.", "D. Bonds and derivatives."],
    ["A. Paying dividends.", "B. Financing short-term operations.", "C. Financing the long-term investments of the bond issuer.", "D. Buying back shares."],
    ["A. Only sovereign national governments.", "B. Only corporations.", "C. Sovereign national governments and corporations.", "D. Only local governments."],
    ["A. The date of the first coupon payment.", "B. The date on which the bond was issued.", "C. The date on which the final cash flow is to be paid.", "D. The date on which the bond is traded."],
    ["A. Sovereign bonds.", "B. Corporate bonds.", "C. Asset-backed securities.", "D. Equity-backed securities."],
    ["A. A regular periodic dividend.", "B. A one-time payment at maturity.", "C. A regular periodic coupon.", "D. Variable interest based on stock price."],
    ["A. Fixed-rate notes.", "B. Bullet bonds.", "C. Floating-rate notes (FRNs).", "D. Zero-coupon bonds."],
    ["A. Credit spread.", "B. Coupon rate.", "C. Market reference rate (MRR).", "D. Base rate."],
    ["A. Percentage points.", "B. Basis points.", "C. Decimal points.", "D. Fractions."],
    ["A. Bullet loan.", "B. Floating loan.", "C. Amortizing loan.", "D. Zero-coupon loan."]
],

"answers": [
    "C. Loans and bonds.",
    "C. Financing the long-term investments of the bond issuer.",
    "C. Sovereign national governments and corporations.",
    "C. The date on which the final cash flow is to be paid.",
    "C. Asset-backed securities.",
    "C. A regular periodic coupon.",
    "C. Floating-rate notes (FRNs).",
    "C. Market reference rate (MRR).",
    "B. Basis points.",
    "C. Amortizing loan."
],
    "references": [
        "[Page: 13,14]",
        "[Page: 13,14]",
        "[Page: 14]",
        "[Page: 14]",
        "[Page: 14]",
        "[Page: 13,14]",
        "[Page: 21,22]",
        "[Page: 21,22]",
        "[Page: 21,22]",
        "[Page: 20]"
    ]
},
            "Fixed-Income Cash Flows and Types": {
    "questions": [
        "What is a typical bond's cash flow structure?",
        "What is an amortizing loan?",
        "What is the principal repayment structure of a bullet bond?",
        "What is the term for bonds that pay interest based on the prevailing market rate at each coupon payment?",
        "What is the variable market rate of interest on a floating-rate note called?",
        "How is the added margin on a floating-rate note typically expressed?",
        "Which institutions often invest in long-term, investment-grade securities to match their long-term liabilities?",
        "What are the major classifications of bond issuers?",
        "What do central banks often use intermediate-term Treasury notes for?",
        "What is the key difference between fixed-income indexes and equity indexes?"
    ],
"choices": [
    ["A. Principal and interest payments at each coupon date.", "B. Principal paid back in a single payment at maturity with periodic interest payments.", "C. Fixed payments of both principal and interest at every coupon date.", "D. Interest payments only, with no repayment of principal."],
    ["A. A loan that continually decreases in value.", "B. A loan with periodic payments including both interest and some repayment of principal.", "C. A loan with no interest payments.", "D. A loan that requires only one lump-sum payment at the end."],
    ["A. Principal is repaid gradually over time.", "B. Principal is never repaid.", "C. Principal is repaid in a single payment at maturity.", "D. Principal is repaid at each coupon date."],
    ["A. Fixed-rate bonds.", "B. Floating-rate notes.", "C. Amortizing bonds.", "D. Zero-coupon bonds."],
    ["A. Yield rate.", "B. Coupon rate.", "C. Market reference rate.", "D. Fixed interest rate."],
    ["A. In percentage points.", "B. In decimal points.", "C. In fractions.", "D. In basis points."],
    ["A. Commercial banks.", "B. Hedge funds.", "C. Pension funds and insurance companies.", "D. Central banks."],
    ["A. Only governments.", "B. Governments, corporates, and investment funds.", "C. Governments, special purpose entities, and municipalities.", "D. Governments, corporates, and special purpose entities issuing asset-backed securities."],
    ["A. To match long-term liabilities.", "B. To finance government operations.", "C. As a monetary policy tool to manage monetary reserves.", "D. As collateral for loans."],
    ["A. Fixed-income indexes have more constituents than equity indexes.", "B. Equity indexes have more constituents than fixed-income indexes.", "C. Fixed-income indexes are only based on government bonds.", "D. Equity indexes have multiple classifications."]
],
    "answers": ["b", "b", "c", "b", "c", "d", "c", "d", "c", "a"],
    "references": [
        "[Page: 20]",
        "[Page: 20]",
        "[Page: 20]",
        "[Page: 20]",
        "[Page: 20]",
        "[Page: 20]",
        "[Page: 32,33]",
        "[Page: 14]",
        "[Page: 32,33]",
        "[Page: 32,33]"
    ]
},
            "Fixed-Income Issuance and Trading": {
    "questions": [
        "What is the primary function of the fixed-income market?",
        "What are the two main categories of fixed-income securities?",
        "What is a bond's maturity?",
        "What is the primary role of financial intermediaries in the fixed-income market?",
        "What is a key characteristic of over-the-counter (OTC) trading in fixed-income securities?",
        "What is a bond's yield to maturity (YTM)?",
        "What is a key advantage of investing in government bonds?"
    ],
"choices": [
    ["A. Facilitating stock trading.", "B. Financing long-term projects.", "C. Trading commodities.", "D. Managing currency exchange."],
    ["A. Government bonds and corporate bonds.", "B. Equities and derivatives.", "C. Real estate and stocks.", "D. Municipal bonds and foreign exchange."],
    ["A. The date it was issued.", "B. The date of its first coupon payment.", "C. The date on which it was purchased.", "D. The date on which the principal is repaid."],
    ["A. Issuing government bonds.", "B. Providing liquidity and matching buyers with sellers.", "C. Regulating the market.", "D. Investing in corporate bonds."],
    ["A. It occurs on organized exchanges.", "B. It involves standardized contracts.", "C. It is always executed electronically.", "D. It often involves customized contracts and is not centralized."],
    ["A. The interest rate paid by the issuer.", "B. The current market price of the bond.", "C. The total interest paid over the life of the bond.", "D. The rate of return an investor can expect if the bond is held until maturity."],
    ["A. High-risk, high-reward potential.", "B. Guaranteed principal repayment.", "C. High trading volume.", "D. Frequent coupon payments."]
],
    "answers": ["b", "a", "d", "b", "d", "d", "b"],
    "references": [
        "[Page: 50]",
        "[Page: 51]",
        "[Page: 51]",
        "[Page: 51]",
        "[Page: 52]",
        "[Page: 54]",
        "[Page: 51]"
    ]
},
            "Fixed-Income Markets for Corporate Issuers": {
    "questions": [
        "1. Which type of external loan financing allows banks to refuse to lend if circumstances change?",
        "2. What is the term for the risk that a company will not be able to sell new commercial paper to replace maturing paper?",
        "3. Which type of credit is typically for a longer term and places restrictive covenants on borrowers?",
        "4. What does factoring refer to?",
        "5. Commercial and retail deposits are a major short-term funding source for which type of institutions?",
        "6. Commercial paper in the United States is typically issued as a ________.",
        "7. What is the purpose of backup lines of credit with banks in relation to commercial paper?"
    ],
    "choices": [
        ["A. Committed line of credit", "B. Revolving line of credit", "C. Uncommitted line of credit"],
        ["A. Credit risk", "B. Rollover risk", "C. Liquidity risk"],
        ["A. Uncommitted line of credit", "B. Committed line of credit", "C. Revolving (operating) line of credit"],
        ["A. Transfer of credit granting and collection of receivables to a lender", "B. Pledging assets as collateral", "C. Issuing short-term unsecured debt securities"],
        ["A. Nonfinancial companies", "B. Asset management firms", "C. Banks"],
        ["A. Coupon security", "B. Pure discount security", "C. Par value security"],
        ["A. To increase the company's credit rating", "B. To provide funds to make repayments on CP when it matures", "C. To issue new commercial paper"]
    ],
    "answers": ["C", "B", "C", "A", "C", "B", "B"],
    "references": [
        "[Pages: 38] A bank extends an offer of credit for a principal amount (credit line), usually charging a floating market reference rate (MRR) plus a fixed credit spread on funds drawn down. The credit is “uncommitted” in the sense that the bank may refuse to lend if circumstances change.",
        "[Pages: 39] CP is often reissued, or “rolled over,” when it matures. The risk that a company will not be able to sell new CP to replace maturing paper is termed rollover risk.",
        "[Pages: 38] Revolving (operating) line of credit. An even more reliable source of short-term financing than a committed line of credit, “revolvers” are typically for a longer term, sometimes years (with potential medium-term loan facilities).",
        "[Pages: 39] Factoring refers to the actual transfer of credit granting and collection of receivables to a lender (“factor”) at a discount from their face value.",
        "[Pages: 40] Commercial and retail deposits are a major short-term funding source for banks.",
        "[Pages: 39] Similar to U.S. T-bills, CP in the United States is typically issued as a pure discount security, making a single payment equal to the face value at maturity.",
        "[Pages: 39] CP is often reissued, or “rolled over,” when it matures. To manage this risk, borrowers maintain backup lines of credit with banks. These are sometimes referred to as liquidity enhancement or backup liquidity lines, whereby lenders agree to provide funds to make repayments on CP when it matures, if needed."
    ]
},
            "Fixed-Income Markets for Government Issuers": {
    "questions": [
        "1. Which bonds are referred to as on-the-run bonds?",
        "2. Which type of investors may have 'noneconomic' objectives when investing in government securities?",
        "3. Bonds issued by the World Bank are best described as?",
        "4. What is the risk associated with governments relying too heavily on short-term debt?",
        "5. Market participants use government debt yields as benchmarks to measure the credit risk of what?",
        "6. Which institutions often rely on government debt in their interest rate risk management?",
        "7. Who uses government debt of various maturities to conduct monetary policy?",
        "8. What is the market discount rate appropriate for discounting a bond’s cash flows called?",
        "9. What is the benefit of having liquid markets in longer maturities of government debt?",
        "10. Who issues nonsovereign government bonds?"
    ],
    "choices": [
        ["A. Most recently issued government securities of a particular maturity", "B. Bonds with the highest yield", "C. Bonds with the longest maturity"],
        ["A. Hedge funds", "B. Central banks", "C. Corporate investors"],
        ["A. Quasi-government bonds", "B. Global bonds", "C. Sovereign bonds"],
        ["A. Interest rate risk", "B. Credit risk", "C. Rollover risk"],
        ["A. Corporate stocks", "B. Non-government debt", "C. Foreign exchange rates"],
        ["A. Retail investors", "B. Asset managers and financial institutions", "C. Governments"],
        ["A. Commercial banks", "B. Central banks", "C. Investment banks"],
        ["A. Coupon rate", "B. Interest rate", "C. Yield to maturity (YTM)"],
        ["A. Increased liquidity", "B. Decreased credit risk", "C. Increased rollover risk"],
        ["A. Corporations", "B. States, provinces, counties, and municipalities", "C. Central banks"]
    ],
    "answers": ["A", "B", "A", "C", "B", "B", "B", "C", "A", "B"],
    "references": [
        "[Pages: 51] Once issued, sovereign debt typically trades in quote-driven OTC dealer markets in a similar fashion to corporate bonds. Trading is most active, and prices most informative, for the most recently issued government securities of a particular maturity. These issues are referred to as on-the-run bonds...",
        "[Pages: 51] Investors in government securities may have 'noneconomic' objectives. For example, government bonds are often used by central banks to conduct monetary policy...",
        "[Pages: 53] Bonds issued by the World Bank are best described as: A. quasi-government bonds.",
        "[Pages: 49] While governments have a great deal of flexibility as to how much short-term debt they issue, relying too heavily on it creates rollover risk.",
        "[Pages: 49] Market participants use government debt yields as benchmarks against which to measure the credit risk of non-government debt.",
        "[Pages: 49] Asset managers and financial institutions often rely on government debt in their interest rate risk management...",
        "[Pages: 49] Central banks buy and sell government debt of various maturities to conduct monetary policy.",
        "[Pages: 54] The market discount rate appropriate for discounting a bond’s cash flows is called the bond’s yield to maturity (YTM).",
        "[Pages: 49] Having liquid markets in longer maturities of government debt also has benefits.",
        "[Pages: 50] Nonsovereign government bonds are issued by states, provinces, counties, and municipalities."
    ]
},
            "Fixed-Income Bond Valuation: Prices and Yields ": {
    "questions": [
        "What is the relationship between a bond's price and its yield-to-maturity (YTM)?",
        "Which bond feature has a more sensitive price to a change in yield?",
        "How does the price of a bond with a longer maturity react to a change in yield compared to a bond with a shorter maturity?",
        "What is the relationship between a bond's price and YTM in terms of convexity?",
        "What is the bond's full price also known as?",
        "What is matrix pricing?",
        "How is the flat price of a bond derived?"
    ],
"choices": [
    ["A. Directly proportional", "B. Inversely related", "C. No relationship"],
    ["A. Higher coupon rate", "B. Lower coupon rate", "C. Equal coupon rate"],
    ["A. Less sensitive", "B. More sensitive", "C. Equally sensitive"],
    ["A. Linear", "B. Concave", "C. Convex"],
    ["A. Flat price", "B. Invoice price", "C. Yield price"],
    ["A. A method to estimate the bond's future price", "B. A method of estimating the required YTM of bonds that are not traded or infrequently traded", "C. A method to determine the bond's coupon rate"],
    ["A. Full price + Accrued interest", "B. Full price - Accrued interest", "C. Full price / Accrued interest"]
],
    "answers": ["B", "B", "B", "C", "B", "B", "B"],
    "references": [
        "[Pages: 58] At a point in time, a decrease (increase) in a bond’s YTM will increase (decrease) its price. That is, there is an inverse relationship between yield and price.",
        "[Pages: 58] Other things equal, the price of a bond with a lower coupon rate is more sensitive to a change in yield than is the price of a bond with a higher coupon rate.",
        "[Pages: 58] Other things equal, the price of a bond with a longer maturity is more sensitive to a change in yield than is the price of a bond with a shorter maturity.",
        "[Pages: 58] The percentage decrease in value when the YTM increases by a given amount is smaller than the increase in value when the YTM decreases by the same amount (the price-yield relationship is convex).",
        "[Pages: 57] A bond’s full price (also known as its invoice price or dirty price) is the sum of its flat price and the accrued interest.",
        "[Pages: 58] Matrix pricing is a method of estimating the required YTM (or price) of bonds that are not traded or infrequently traded.",
        "[Pages: 57] Flat price = full price - accrued interest"
    ]
},
            "Yield and Yield Spread Measures for Fixed-Rate Bonds ": {
    "questions": [
        "What is a yield spread, or benchmark spread?",
        "What is the spread known as when it's relative to a government bond yield?",
        "How is the G-spread calculated?",
        "What are I-spreads frequently stated for?",
        "What does a zero-volatility spread or Z-spread account for?",
        "What can be observed from the prices of zero-coupon bonds?",
        "What do yields earned by individual cash flows at different maturities refer to?"
    ],
    "choices": [
        ["A. The difference between the yields of a bond and a benchmark security.", "B. The difference between the coupon rate of a bond and its yield.", "C. The difference between the maturity of a bond and its benchmark."],
        ["A. I-spread", "B. Z-spread", "C. G-spread"],
        ["A. By subtracting the bond's yield from the benchmark yield.", "B. By adding the bond's yield to the benchmark yield.", "C. By multiplying the bond's yield with the benchmark yield."],
        ["A. Bonds denominated in US dollars.", "B. Bonds denominated in euros.", "C. Bonds denominated in yen."],
        ["A. The difference between the yields of a specific bond and a benchmark.", "B. The shape of the benchmark yield curve.", "C. The credit risk of the issuer."],
        ["A. Different individual cash flows at different maturities can have different yields.", "B. All individual cash flows have the same yield.", "C. The yield of a zero-coupon bond is always zero."],
        ["A. Spot rates", "B. Coupon rates", "C. Benchmark rates"]
    ],
    "answers": ["A", "C", "A", "B", "B", "A", "A"],
    "references": [
        "[Pages: 68] A yield spread, or benchmark spread, is the difference between the yields of a bond and a benchmark security.",
        "[Pages: 68] A yield spread in basis points over a government bond is also known as a G-spread.",
        "[Pages: 68] Then, the G-spread = 6.82% - 4.33% = 2.49%, or 249 basis points.",
        "[Pages: 69] I-spreads are frequently stated for bonds denominated in euros.",
        "[Pages: 69] The G-spread and I-spread are based on the difference between the yields of a specific bond and a benchmark.",
        "[Pages: 69] We can observe from the prices of zero-coupon bonds that different individual cash flows occurring at different maturities can have different yields.",
        "[Pages: 69] Yields earned by individual cash flows at different maturities are referred to as spot rates."
    ]
},
            "The Term Structure of Interest Rates: Spot, Par, and Forward Curves": {
  "questions": [
    "What are spot rates?",
    "What does the single YTM of a coupon-paying bond represent?",
    "What is the significance of calculating spreads over benchmark spot rates?",
    "What is the purpose of a method that derives a bond's yield spread to a benchmark spot yield curve?",
    "What can cause an increase in a bond's yield?"
  ],
  "choices": [
    ["A. Rates offered by individual cash flows of a bond.", "B. Rates that represent the average yield of a bond.", "C. Rates that are used for interest rate swaps.", "D. Rates that are used as benchmarks for government bonds."],
    ["A. A weighted average of the different spot rates.", "B. The highest yield offered by the bond.", "C. The lowest yield offered by the bond.", "D. The yield of the benchmark bond."],
    ["A. It provides a less precise way of calculating spreads.", "B. It is based solely on the YTM of the bond.", "C. It better captures how rates vary over different maturities.", "D. It is used only for government bonds."],
    ["A. To subtract an equal amount from each benchmark spot rate.", "B. To add an equal amount to each benchmark spot rate.", "C. To calculate the bond's YTM.", "D. To determine the bond's credit risk."],
    ["A. Only the real risk-free rate.", "B. Only the expected inflation rate.", "C. Both macroeconomic and microeconomic factors.", "D. Neither the real risk-free rate nor the expected inflation rate."]
  ],
  "answers": ["A", "A", "C", "B", "C"],
  "references": [
    "[Page 69]",
    "[Page 69]",
    "[Page 69]",
    "[Page 69]",
    "[Page 69]"
  ]
},      
            "Interest Rate Risk and Return": {
  "questions": [
    "What are the three sources of returns from investing in a fixed-rate bond?",
    "What is the rate of return for an investor who holds a fixed-rate bond to maturity and the YTM of the bond does not change over its life?",
    "For an investor with a short investment horizon, which risk is more significant?",
    "What is the significance of a bond investor's horizon yield?",
    "If the market YTM for a bond decreases after the bond is purchased but before the first coupon date, what will be the rate of return for a bond investor if the bond is held for a long period?"
  ],
  "choices": [
    ["A. Coupon payments, interest on reinvested coupons, and capital gains or losses.", "B. Coupon payments, principal payments, and interest on reinvested coupons.", "C. Principal payments, capital gains or losses, and interest rate changes.", "D. Coupon payments, interest rate changes, and capital gains or losses."],
    ["A. YTM of the bond when purchased.", "B. Prevailing market rate.", "C. Average of the coupon rate and YTM.", "D. Rate of reinvested coupon payments."],
    ["A. Reinvestment risk.", "B. Price risk.", "C. Credit risk.", "D. Default risk."],
    ["A. It represents the YTM of the bond.", "B. It is the compound annual return earned from the bond over the investment horizon.", "C. It is the average yield of the bond over its life.", "D. It represents the bond's credit risk premium."],
    ["A. Higher than the YTM at bond purchase.", "B. Equal to the YTM at bond purchase.", "C. Lower than the YTM at bond purchase.", "D. Equal to the prevailing market rate."]
  ],
  "answers": ["A", "A", "B", "B", "C"],
  "references": [
    "[Page 88]",
    "[Page 88]",
    "[Pages 92-93]",
    "[Page 89]",
    "[Page 88]"
  ]
},
            "Yield-Based Bond Duration Measures and Properties": {
  "questions": [
    "What is key rate duration also known as?",
    "What does effective duration separate the effects of?",
    "What is the difference between effective duration and the methods previously discussed?",
    "What is empirical duration estimated from?",
    "In which scenario might empirical duration be lower than analytical duration?"
  ],
  "choices": [
    ["A. Effective duration", "B. Modified duration", "C. Partial duration", "D. Convexity duration"],
    ["A. Changes in benchmark yields from changes in the spread for credit and liquidity risk.", "B. Changes in credit risk from changes in liquidity risk.", "C. Changes in YTM from changes in benchmark yields.", "D. Changes in coupon payments from changes in principal payments."],
    ["A. Effective duration is based on changes in YTM.", "B. Effective duration makes no distinction between changes in the benchmark yield and changes in the spread.", "C. Effective duration reflects only the sensitivity of the bond’s value to changes in the benchmark yield curve.", "D. Effective duration is based on changes in the benchmark yield curve."],
    ["A. Analytical models", "B. Historical data using models", "C. Benchmark yield curves", "D. Credit risk assessments"],
    ["A. For credit-risky bonds in a flight-to-quality scenario.", "B. For bonds with high liquidity.", "C. For bonds with a flat yield curve.", "D. For bonds with embedded options in a high-yield environment."]
  ],
  "answers": ["C", "A", "C", "B", "A"],
  "references": [
    "[Page 114]",
    "[Page 112]",
    "[Page 112]",
    "[Page 116]",
    "[Page 116]"
  ]
},
            "Yield-Based Bond Convexity and Portfolio Properties": {
    "questions": [
        "What does convexity refer to in the context of a bond's price-yield relationship?",
        "How can convexity of a coupon-paying bond be calculated?",
        "What is the limitation of portfolio duration based on weighted average durations of constituents of the portfolio?",
        "How can the convexity adjustment to the price change be described for a bond with positive convexity?",
        "What is the significance of effective convexity?"
    ],
    "choices": [
        ["A) The slope of the price-yield curve.", "B) The curvature of the bond’s price-yield relationship.", "C) The linear approximation of the price-yield relationship.", "D) The inverse relationship between price and yield."],
        ["A) By considering each of a bond’s cash flows separately.", "B) By using the bond's YTM.", "C) By taking the inverse of the bond's duration.", "D) By using the bond's coupon rate."],
        ["A) It assumes yields change uniformly across all maturities.", "B) It assumes the portfolio does not include bonds with embedded options.", "C) It assumes the portfolio’s internal rate of return is equal to its cash flow yield.", "D) It assumes a non-parallel shift of the yield curve."],
        ["A) The duration-only based estimate of the increase in price resulting from a decrease in yield is too low.", "B) The duration-only based estimate of the decrease in price resulting from an increase in yield is too high.", "C) Both A and B.", "D) Neither A nor B."],
        ["A) It is based on changes in the bond’s YTM.", "B) It is based on changes in the benchmark curve.", "C) It separates the effects of changes in benchmark yields from changes in the spread for credit and liquidity risk.", "D) It is the inverse of effective duration."]
    ],
    "answers": [
        "B) The curvature of the bond’s price-yield relationship.",
        "A) By considering each of a bond’s cash flows separately.",
        "A) It assumes yields change uniformly across all maturities.",
        "C) Both A and B.",
        "B) It is based on changes in the benchmark curve."
    ],
    "references": [
        "[Page 108] Convexity refers to the curvature of a bond’s price-yield relationship.",
        "[Page 104] One way to calculate convexity is by considering each of a bond’s cash flows separately.",
        "[Page 107] One limitation of this approach is that it assumes the YTM of every bond (of any maturity) in the portfolio must change by the same amount.",
        "[Page 106] The convexity adjustment to the price change is the same for either an increase or a decrease in yield. As illustrated in Figure 60.2, the duration-only based estimate of the increase in price resulting from a decrease in yield is too low for a bond with positive convexity, and it is improved by a positive adjustment for convexity. The duration-only based estimate of the decrease in price resulting from an increase in yield is larger than the actual decrease, so it is also improved by a positive adjustment for convexity.",
        "[Page 112] Effective convexity (EffCon), which is once again based on changes in the benchmark curve, rather than on changes in the bond’s YTM."
    ]
},
            "Curve-Based and Empirical Fixed-Income Risk Measures": {
  "questions": [
    "Why are effective duration and effective convexity the most appropriate measures of interest rate risk for bonds with embedded options?",
    "What is key rate duration?",
    "What is shaping risk?",
    "What is the difference between empirical duration and analytical duration?",
    "Why is effective duration more appropriate than modified duration for estimating interest rate risk for bonds with embedded options?"
  ],
  "choices": [
    ["A. They account for the bond's credit risk.", "B. They consider the bond's YTM.", "C. They account for uncertain cash flows that depend on the path of interest rate changes.", "D. They are based on the bond's coupon rate."],
    ["A. It is the sensitivity of the value of a bond to changes in its YTM.", "B. It is the sensitivity of the value of a bond or portfolio to changes in the benchmark yield for a specific maturity.", "C. It is the inverse of the bond's effective duration.", "D. It is the bond's coupon rate."],
    ["A. It is the risk of a bond defaulting.", "B. It is the risk of interest rates changing uniformly across all maturities.", "C. It is the effect of a nonparallel shift in the yield curve on a bond portfolio.", "D. It is the risk associated with reinvesting coupon payments."],
    ["A. Empirical duration is based on historical data, while analytical duration is based on mathematical formulas.", "B. Empirical duration is used for bonds with embedded options, while analytical duration is used for option-free bonds.", "C. Empirical duration accounts for the effect of changes in benchmark yields on risky credits, while analytical duration does not.", "D. Empirical duration is the inverse of analytical duration."],
    ["A. They tend to have greater credit risk than option-free bonds.", "B. They exhibit high convexity that makes modified duration less accurate.", "C. They have uncertain cash flows that depend on the path of interest rate changes.", "D. They are based on the bond's coupon rate."]
  ],
  "answers": [
    "C. They account for uncertain cash flows that depend on the path of interest rate changes.",
    "B. It is the sensitivity of the value of a bond or portfolio to changes in the benchmark yield for a specific maturity.",
    "C. It is the effect of a nonparallel shift in the yield curve on a bond portfolio.",
    "C. Empirical duration accounts for the effect of changes in benchmark yields on risky credits, while analytical duration does not.",
    "C. They have uncertain cash flows that depend on the path of interest rate changes."
  ],
  "references": [
    "[Page 111]",
    "[Page 114]",
    "[Page 114]",
    "[Page 115]",
    "[Page 115]"
  ]
},
            "Credit Risk": {
  "questions": [
    "What does credit risk refer to?",
    "Which of the following is NOT a bottom-up credit analysis factor?",
    "How is expected loss measured in terms of credit risk?",
    "What is the primary concern for investment grade bond investors regarding credit spread risk?",
    "Which of the following is NOT a reason investors should be cautious about relying exclusively on credit ratings?",
    "What is a key concern regarding the character of management that may impact the creditworthiness of the issuer?",
    "Which of the following is NOT a top-down credit analysis factor?"
  ],
  "choices": [
    ["A. The possibility of a borrower's assets depreciating in value.", "B. The possibility that a borrower fails to make the scheduled interest payments or return of principal.", "C. The risk of fluctuating interest rates.", "D. The risk associated with foreign exchange rates."],
    ["A. Capacity", "B. Collateral", "C. Currency", "D. Covenants"],
    ["A. Expected loss = probability of default + loss given default", "B. Expected loss = probability of default × loss given default", "C. Expected loss = (probability of default / loss given default) + 1", "D. Expected loss = 1 - (probability of default × loss given default)"],
    ["A. The risk of default occurring suddenly.", "B. The risk that yield spreads widen due to deteriorating conditions.", "C. The risk of interest rates dropping significantly.", "D. The risk of the bond being called early."],
    ["A. Rating agencies cannot always judge credit risk accurately.", "B. Market prices of bonds often adjust more rapidly than credit ratings.", "C. Credit ratings always reflect the current market conditions.", "D. Firms are subject to the risk of unforeseen events that credit ratings do not reflect."],
    ["A. The use of aggressive accounting policies.", "B. The number of years the management has been in the industry.", "C. The educational background of the management team.", "D. The management's personal investment portfolio."],
    ["A. Conditions", "B. Country", "C. Capital", "D. Currency"]
  ],
  "answers": [
    "B. The possibility that a borrower fails to make the scheduled interest payments or return of principal.",
    "C. Currency",
    "B. Expected loss = probability of default × loss given default",
    "B. The risk that yield spreads widen due to deteriorating conditions.",
    "C. Credit ratings always reflect the current market conditions.",
    "A. The use of aggressive accounting policies.",
    "C. Capital"
  ],
  "references": [
    "[Page 126]",
    "[Page 118]",
    "[Page 119]",
    "[Page 123]",
    "[Page 122-123]",
    "[Page 134]",
    "[Page 118]"
  ]
},
            "Credit Analysis for Corporate Issuers": {
  "questions": [
    "Which of the following is a qualitative factor that implies a corporate issuer has high creditworthiness?",
    "How can profitability be measured in credit analysis for corporate issuers?",
    "Which of the following is NOT a leverage ratio used in credit analysis for corporate issuers?",
    "What does secured debt have a priority over?",
    "Which of the following ratings is typically based on a company's senior unsecured debt?",
    "What is a concern when considering the character of management in credit analysis?",
    "Which of the following is a top-down credit analysis factor?"
  ],
  "choices": [
    ["A. High levels of competition in the industry.", "B. Having a stable business model.", "C. High business risk.", "D. Frequent changes in corporate governance."],
    ["A. Profitability = EBIT / total assets.", "B. Profitability = EBIT / equity.", "C. Profitability = EBIT / revenue.", "D. Profitability = EBIT / net income."],
    ["A. Debt to EBITDA.", "B. Retained cash flow to net debt.", "C. Debt to equity.", "D. EBIT to interest expense."],
    ["A. Equity.", "B. Unsecured debt.", "C. Both equity and unsecured debt.", "D. Neither equity nor unsecured debt."],
    ["A. Corporate family ratings (CFRs).", "B. Corporate credit ratings (CCRs).", "C. Bond ratings.", "D. Equity ratings."],
    ["A. Use of aggressive accounting policies.", "B. Number of years the company has been in operation.", "C. Total number of employees in the company.", "D. The company's market capitalization."],
    ["A. Conditions.", "B. Capital.", "C. Collateral.", "D. Character."]
  ],
  "answers": [
    "B. Having a stable business model.",
    "C. Profitability = EBIT / revenue.",
    "D. EBIT to interest expense.",
    "C. Both equity and unsecured debt.",
    "A. Corporate family ratings (CFRs).",
    "A. Use of aggressive accounting policies.",
    "A. Conditions."
  ],
  "references": [
    "[Page 138]",
    "[Page 139]",
    "[Page 139]",
    "[Page 139]",
    "[Page 137]",
    "[Page 134]",
    "[Page 132]"
  ]
},
            "Fixed-Income Securitization": {
    "questions": [
        "What is one of the benefits of securitization for issuers?",
        "Which of the following is NOT a risk to investors in ABSs?",
        "What is the primary role of a special purpose entity (SPE) in the securitization process?",
        "What is one of the benefits of securitization for investors?",
        "In the context of securitization, who typically acts as the originator?",
        "What does the term 'bankruptcy remote' in the context of securitization imply?",
        "Who is appointed to oversee the safekeeping of collateral and cash flows due to the ABS investors?"
    ],
    "choices": [
        ["A) Increased credit risk", "B) Lower leverage", "C) Reduced liquidity", "D) Higher interest rates"],
        ["A) Uncertain cash flows from collateral", "B) Credit risk of the collateral", "C) Guaranteed fixed returns", "D) Systemic buildup of credit risk"],
        ["A) To make loans", "B) To issue asset-backed securities", "C) To buy automobiles", "D) To manage the originator's balance sheet"],
        ["A) Reduced access to collateral pool", "B) Increased credit risk", "C) Tailored risk and return", "D) Lowered profitability"],
        ["A) The bank making loans", "B) The special purpose entity", "C) The asset-backed security holder", "D) The trustee"],
        ["A) The originator is likely to go bankrupt", "B) The SPE is financially intertwined with the originator", "C) The value of ABS claims is affected by the financial position of the originator", "D) The SPE's financial position is separate from the originator's"],
        ["A) The originator", "B) The special purpose entity", "C) The trustee", "D) The servicer"]
    ],
    "answers": ["B) Lower leverage", "C) Guaranteed fixed returns", "B) To issue asset-backed securities", "C) Tailored risk and return", "A) The bank making loans", "D) The SPE's financial position is separate from the originator's", "C) The trustee"],
    "references": [
        "[Page 141]",
        "[Page 141]",
        "[Page 139-140]",
        "[Page 141]",
        "[Page 139]",
        "[Page 142-143]",
        "[Page 142-143]"
    ]
},
            "Asset-Backed Security (ABS) Instrument and Market Features": {
    "questions": [
        "1. What do the cash flows to a pool of credit card receivables include?",
        "2. What happens during the lockout period of a credit card ABS?",
        "3. What is the significance of the revolving period of a credit card ABS in terms of prepayment risk?",
        "4. What starts after the lockout period of a credit card ABS ends?",
        "5. What are solar ABSs backed by?",
        "6. How are credit card receivables described in terms of amortization?",
        "7. What is a key distinction between debt-based assets acting as collateral for ABSs?"
    ],
    "choices": [
        ["A. Interest rates, B. Membership fees, C. Principal repayments, D. All of the above"],
        ["A. ABS investors receive both interest and principal, B. ABS investors only receive interest and fees, C. ABS investors only receive principal"],
        ["A. Investors are subject to high prepayment risk, B. Investors are not subject to prepayment risk, C. Prepayment risk is unpredictable"],
        ["A. Lockout period, B. Revolving period, C. Amortization period, D. Pre-funding period"],
        ["A. Credit card receivables, B. Business loans, C. Loans for homeowners to install solar panels, D. Music royalties"],
        ["A. Amortizing, B. Nonamortizing, C. Variable, D. Fixed"],
        ["A. Interest rate, B. Credit rating, C. Whether it is amortizing or nonamortizing, D. Maturity date"]
    ],
    "answers": [
        "D. All of the above",
        "B. ABS investors only receive interest and fees",
        "B. Investors are not subject to prepayment risk",
        "C. Amortization period",
        "C. Loans for homeowners to install solar panels",
        "B. Nonamortizing",
        "C. Whether it is amortizing or nonamortizing"
    ],
    "references": [
        "The cash flow to a pool of credit card receivables includes finance charges (i.e., interest), membership and late payment fees, and principal repayments. ",
        "A credit card securitization structure will typically include a lockout period or revolving period during which ABS investors only receive interest and fees paid on the collateral.",
        "During the revolving period of a credit card ABS, investors are not subject to prepayment risk because any principal payments in the underlying collateral are used to make additional loans",
        "Once the lockout period ends, the amortization period of the ABS begins, and principal payments made on the underlying collateral are passed through to security holders",
        "Solar ABSs are backed by loans to homeowners to finance installation of domestic solar energy equipment. ",
        "Credit card ABSs are backed by credit card receivables, which are nonamortizing receivables. ",
        "A key distinction between the debt-based assets acting as collateral for these ABSs is whether it is amortizing or nonamortizing"
    ]
},   
            "Mortgage-Backed Security (MBS) Instrument and Market Features": {
    "questions": [
        "What does the loan-to-value ratio (LTV) indicate?",
        "What are agency residential mortgage-backed securities (RMBSs) guaranteed and issued by?",
        "What do investors in mortgage pass-through securities receive?",
        "What is a residential mortgage loan?",
        "How are MBSs similar to?",
        "What does the weighted average maturity (WAM) of the pool represent?",
        "What is the significance of the weighted average coupon (WAC) of the pool?"
    ],
    "choices": [
        ["A. The percentage of the value of the real estate collateral that is loaned.", "B. The size of the monthly debt payments of the borrower.", "C. The interest rate of the mortgage.", "D. The maturity of the mortgage."],
        ["A. Private companies", "B. The federal government or a government-sponsored enterprise", "C. International financial institutions", "D. Municipalities"],
        ["A. Only the principal payments from the underlying pool of mortgages.", "B. The monthly cash flows generated by the underlying pool of mortgages, less any servicing and guarantee/insurance fees.", "C. The full interest and principal payments without any deductions.", "D. Only the interest payments from the underlying pool of mortgages."],
        ["A. A loan for commercial real estate.", "B. A loan for which the collateral is residential real estate.", "C. A loan for purchasing vehicles.", "D. A loan for business operations."],
        ["A. Non-callable bonds", "B. Callable bonds", "C. Zero-coupon bonds", "D. Convertible bonds"],
        ["A. The average interest rate of all the mortgages in the pool.", "B. The average size of all the mortgages in the pool.", "C. The weighted average of the final maturities of all the mortgages in the pool.", "D. The average duration of all the mortgages in the pool."],
        ["A. It represents the average credit rating of the mortgages.", "B. It is the weighted average of the interest rates of all the mortgages in the pool.", "C. It indicates the average size of the mortgages.", "D. It represents the average duration of the mortgages."]
    ],
    "answers": [
        "A. The percentage of the value of the real estate collateral that is loaned.",
        "B. The federal government or a government-sponsored enterprise",
        "B. The monthly cash flows generated by the underlying pool of mortgages, less any servicing and guarantee/insurance fees.",
        "B. A loan for which the collateral is residential real estate.",
        "B. Callable bonds",
        "C. The weighted average of the final maturities of all the mortgages in the pool.",
        "B. It is the weighted average of the interest rates of all the mortgages in the pool."
    ],
    "references": [
        "The loan-to-value ratio (LTV) indicates the percentage of the value of the real estate collateral that is loaned.",
        "Agency residential mortgage-backed securities (RMBSs) are guaranteed and issued by the federal government or a government-sponsored enterprise.",
        "Investors in mortgage pass-through securities receive the monthly cash flows generated by the underlying pool of mortgages, less any servicing and guarantee/insurance fees.",
        "A residential mortgage loan is a loan for which the collateral that underlies the loan is residential real estate.",
        "MBSs are like callable bonds, where the borrower has the right to repay the loan early.",
        "The weighted average maturity (WAM) of the pool is equal to the weighted average of the final maturities of all the mortgages in the pool.",
        "The weighted average coupon (WAC) of the pool is the weighted average of the interest rates of all the mortgages in the pool."
    ]
}
                    }, 
        "DERIVATIVES":{
            "Derivative Instruments and Markets": {
    "questions": [
        "What is the relationship between the value of a forward contract at initiation and its price?",
        "What happens to the buyer of a forward contract when the market price of the shares at settlement is greater than the forward price?",
        "In a futures contract, what is imposed to limit how much each day’s settlement price can change from the previous day’s settlement price?",
        "What is the primary purpose of multiple-period swaps?",
        "What does the option premium consist of?",
        "What is the significance of the par swap rate in a simple interest-rate swap?",
        "In derivative pricing models, which rate is used to discount future cash flows?",
        "What does replication refer to in the context of derivatives?",
        "What is the primary factor that determines the no-arbitrage forward price of an asset, assuming no costs or benefits of holding the underlying asset?",
        "In a swap contract, what is the price defined as?"
    ],
    "choices": [
        ["A. The value is always positive.", "B. The value is always negative.", "C. The value is zero.", "D. The value is equal to the price."],
        ["A. The buyer incurs a loss.", "B. The buyer gains.", "C. The buyer's position remains neutral.", "D. The buyer has to pay the difference."],
        ["A. Price ceilings", "B. Price floors", "C. Price limits", "D. Price barriers"],
        ["A. To manage currency risk.", "B. To manage interest rate risk.", "C. To manage credit risk.", "D. To manage operational risk."],
        ["A. Exercise value only.", "B. Time value only.", "C. Both exercise value and time value.", "D. Neither exercise value nor time value."],
        ["A. It is the floating rate specified in the swap contract.", "B. It is the fixed rate at which the sum of the present values of the FRAs equals zero.", "C. It represents the average rate of all the swaps in the market.", "D. It is the rate at which the swap is initially priced."],
        ["A. The inflation rate.", "B. The risk-free rate.", "C. The market rate.", "D. The swap rate."],
        ["A. Creating a portfolio with cash market transactions that has the same payoffs as a derivative.", "B. Duplicating the underlying asset in the market.", "C. Creating multiple copies of the same derivative contract.", "D. Replicating the cash flows of the underlying asset."],
        ["A. The spot price adjusted for dividends.", "B. The spot price compounded at the risk-free rate over the time until expiration.", "C. The current market rate of the asset.", "D. The expected future price of the asset."],
        ["A. The floating rate specified in the swap contract.", "B. The average of all rates in the market.", "C. The fixed rate specified in the swap contract.", "D. The rate at which the swap is initially priced."]
    ],
    "answers": [
        "C. The value is zero.",
        "B. The buyer gains.",
        "C. Price limits",
        "B. To manage interest rate risk.",
        "C. Both exercise value and time value.",
        "B. It is the fixed rate at which the sum of the present values of the FRAs equals zero.",
        "B. The risk-free rate.",
        "A. Creating a portfolio with cash market transactions that has the same payoffs as a derivative.",
        "B. The spot price compounded at the risk-free rate over the time until expiration.",
        "C. The fixed rate specified in the swap contract."
    ],
    "references": [
        "The value of a forward contract at initiation is zero.",
        "The buyer of the shares in a forward contract will have gains when the price of the underlying increases.",
        "Many futures contracts have price limits, which are exchange-imposed limits on how much each day’s settlement price can change from the previous day’s settlement price.",
        "Multiple-period swaps are used primarily by investors and issuers to manage interest rate risk.",
        "Option premium = exercise value + time value.",
        "The par swap rate is the fixed rate at which the sum of the present values of these FRAs equals zero.",
        "Derivatives pricing models use the risk-free rate to discount future cash flows.",
        "Replication refers to creating a portfolio with cash market transactions that has the same payoffs as a derivative for all possible future values of the underlying.",
        "Assuming no costs or benefits of holding the underlying asset, the forward price that will prevent arbitrage is the spot price compounded at the risk-free rate over the time until expiration.",
        "The price of a fixed-for-floating interest-rate swap is defined as the fixed rate specified in the swap contract."
    ]
},
            "Forward Commitment and Contingent Claim Features and Instruments": {
  "questions": [
    "1. What is a forward commitment?",
    "2. Which derivative has a future payoff only if a specific future event occurs?",
    "3. How does a futures contract differ from a forward contract in terms of trading?",
    "4. Which contract requires daily cash settlement of gains and losses?",
    "5. Who has long exposure in a forward contract?",
    "6. What is the primary purpose of margin in futures trading?",
    "7. What is the outcome for the buyer of a forward contract if the price of the underlying at the settlement date exceeds the forward price?",
    "8. Which contract is equivalent to a series of forward contracts?",
    "9. Which option gives the owner the right to buy the underlying asset?",
    "10. When is the exercise value of a put option positive at expiration?"
  ],
  "choices": [
    ["A. A legally binding promise for a future action", "B. A claim to a future payoff", "C. A future payment obligation", "D. A future claim to an asset"],
    ["A. Forward Contract", "B. Futures Contract", "C. Option", "D. Swap"],
    ["A. Forwards are exchange-traded", "B. Futures are privately negotiated", "C. Forwards are standardized", "D. Futures are exchange-traded"],
    ["A. Forward Contract", "B. Option", "C. Swap", "D. Futures Contract"],
    ["A. The seller", "B. The buyer", "C. Both the seller and buyer", "D. Neither the seller nor buyer"],
    ["A. To earn interest", "B. To ensure contract fulfillment", "C. To speculate on price movements", "D. To set the contract price"],
    ["A. Profit", "B. Loss", "C. No change", "D. Obligation to buy more"],
    ["A. Option", "B. Swap", "C. Forward Contract", "D. Futures Contract"],
    ["A. Put Option", "B. Call Option", "C. Swap Option", "D. Futures Option"],
    ["A. When the underlying asset price is greater than the exercise price", "B. When the underlying asset price equals the exercise price", "C. When the underlying asset price is less than the exercise price", "D. Always"]
  ],
  "answers": [
    "A", "C", "D", "D", "B", "B", "A", "B", "B", "C"
  ],
  "references": [
    "A forward commitment is a legally binding promise to perform some action in the future. (Page 8)",
    "A contingent claim is a derivative that has a future payoff only if some future event takes place. (Page 8)",
    "A futures contract is quite similar to a forward contract but is standardized and exchange-traded. (Page 8)",
    "Futures are backed by a central clearinghouse and require daily cash settlement of gains and losses. (Page 8)",
    "The buyer has long exposure to the underlying asset in that he will make a profit on the forward if the price of the underlying at the settlement date exceeds the forward price. (Page 8)",
    "On a futures exchange, margin is cash or other acceptable collaterals. (Page 8)",
    "The buyer has long exposure to the underlying asset in that he will make a profit on the forward if the price of the underlying at the settlement date exceeds the forward price. (Page 8)",
    "A swap is an agreement to buy or sell an underlying asset periodically over the life of the swap contract. It is equivalent to a series of forward contracts. (Page 17)",
    "A call gives the owner the right to call an asset away (buy it) from the seller. (Page 17)",
    "The exercise value of a put option is positive at expiration if the underlying asset price is less than the exercise price. (Page 17)"
  ]
},
            "Derivative Benefits, Risks, and Issuer and Investor Uses": {
  "questions": [
    "Which of the following is a potential advantage of derivative instruments over cash market transactions?",
    "How can a manufacturer hedge the exchange rate risk of anticipated receipts or payments?",
    "What information can derivatives prices and trading provide that cash market transactions do not?",
    "Which of the following is an operational advantage of derivatives compared to cash markets?",
    "What can be inferred using interest rate futures across maturities?",
    "How can a corporation with a commodity-like product stabilize the value reported on the balance sheet over time?",
    "Which of the following is a use of derivatives by investors?"
  ],
    "choices": [
        ["A. Ability to Change Risk Allocation", "B. Ability to Predict Future Prices", "C. Ability to Eliminate All Risks", "D. Ability to Avoid Transaction Costs"],
        ["A. By investing in the stock market", "B. By using derivative instruments", "C. By diversifying their product range", "D. By changing their supplier"],
        ["A. Historical data on asset prices", "B. Information on company management", "C. Information Discovery", "D. Information on company dividends"],
        ["A. Higher interest rates", "B. Greater ease of short selling", "C. Longer transaction times", "D. Greater complexity"],
        ["A. The current market prices of derivatives", "B. The historical price volatility of the underlying", "C. Expected future interest rates", "D. The current market demand for bonds"],
        ["A. By diversifying their product range", "B. By selling forward contracts on an underlying that matches well with their product", "C. By investing in the stock market", "D. By changing their supplier"],
        ["A. Hedging against price risk for inventory held", "B. Modifying the risk exposure of a securities portfolio", "C. Stabilizing the balance sheet value of a foreign subsidiary", "D. Predicting future stock prices"]
    ],
    "answers": [
        "A. Ability to Change Risk Allocation",
        "B. By using derivative instruments",
        "C. Information Discovery",
        "B. Greater ease of short selling",
        "C. Expected future interest rates",
        "B. By selling forward contracts on an underlying that matches well with their product",
        "B. Modifying the risk exposure of a securities portfolio"
    ],
  "references": [
    "Page 18",
    "Page 18",
    "Page 18",
    "Page 19",
    "Page 19",
    "Page 21",
    "Page 22"
  ]
},
            "Arbitrage, Replication, and the Cost of Carry in Pricing Derivatives": {
  "questions": [
    "What does the no-arbitrage condition refer to in the context of derivative securities valuation?",
    "What does replication refer to in the context of derivatives?",
    "Assuming no costs or benefits of holding the underlying asset, what determines the forward price that will prevent arbitrage?",
    "What increases the no-arbitrage forward price of an asset?",
    "What decreases the no-arbitrage forward price of an asset?",
    "When deriving the no-arbitrage forward price for an asset, what was assumed regarding the benefits and costs of holding the asset?",
    "In the context of a forward contract on a stock that pays no dividends, how can an investor replicate a forward?"
  ],
     "choices": [
        ["A. Valuing risky assets based on expected future cash flows.", "B. A transaction where an investor realizes a risk-free gain by exploiting price differences.", "C. The process of creating a portfolio with cash market transactions.", "D. The use of risk-adjusted rates for discounting."],
        ["A. The act of copying a portfolio's structure.", "B. Creating a portfolio with cash market transactions that has the same payoffs as a derivative.", "C. The process of determining the no-arbitrage price.", "D. The act of exploiting arbitrage opportunities."],
        ["A. The spot price multiplied by the risk-free rate.", "B. The spot price divided by the risk-free rate.", "C. The spot price compounded at the risk-free rate over the time until expiration.", "D. The spot price minus the risk-free rate."],
        ["A. Greater benefits of holding an asset.", "B. Lower costs of holding an asset.", "C. Greater costs of holding an asset.", "D. Lower benefits of holding an asset."],
        ["A. Lower costs of holding an asset.", "B. Greater benefits of holding an asset.", "C. Lower benefits of holding an asset.", "D. Greater costs of holding an asset."],
        ["A. There were both benefits and costs.", "B. There were no benefits and no costs.", "C. There were benefits but no costs.", "D. There were costs but no benefits."],
        ["A. By selling the underlying short and investing the proceeds at the risk-free rate.", "B. By buying the underlying in the spot market and holding it.", "C. By borrowing at the risk-free rate to buy the underlying.", "D. By investing in a risk-free bond."]
    ],
    "answers": [
        "B. A transaction where an investor realizes a risk-free gain by exploiting price differences.",
        "B. Creating a portfolio with cash market transactions that has the same payoffs as a derivative.",
        "C. The spot price compounded at the risk-free rate over the time until expiration.",
        "D. Lower benefits of holding an asset.",
        "B. Greater benefits of holding an asset.",
        "B. There were no benefits and no costs.",
        "C. By borrowing at the risk-free rate to buy the underlying."
    ],
    "references": [
    "Page 24",
    "Page 25",
    "Page 29",
    "Page 29",
    "Page 29",
    "Page 26",
    "Page 25"
  ]
},
            "Pricing and Valuation of Forward Contracts and for an Underlying with Varying Maturities": {
  "questions": [
    "At the initiation of a forward contract that is priced at its no-arbitrage value, what is the value of the forward?",
    "During the life of a forward contract, how is its value to the buyer determined?",
    "At the expiration of a forward contract, how is the value of the forward to the buyer determined?",
    "If the forward buyer has a gain on the contract, what can be said about the forward seller?",
    "What is the underlying for a derivative?",
    "What is the primary difference between a forward contract and a futures contract?",
    "In a simple interest-rate swap, what does one party typically pay?"
  ],
"choices": [
    ["A. Equal to the spot price.", "B. Equal to the forward price.", "C. Zero.", "D. Equal to the difference between the spot and forward price."],
    ["A. By the current spot price minus the future value of the forward contract price.", "B. By the current spot price minus the present value of the forward contract price.", "C. By the difference between the spot and forward price.", "D. By the forward price minus the current spot price."],
    ["A. By the spot price minus the forward price.", "B. By the forward price minus the spot price.", "C. By the spot price.", "D. By the forward price."],
    ["A. The forward seller has an equal gain.", "B. The forward seller has no impact.", "C. The forward seller has an equal loss.", "D. The forward seller benefits from the gain."],
    ["A. The security that determines the value of a derivative security.", "B. The future date at which the derivative is settled.", "C. The initial price of the derivative.", "D. The final price of the derivative."],
    ["A. The underlying asset.", "B. The contract size.", "C. The settlement date.", "D. The liquidity and regulation."],
    ["A. A floating rate.", "B. A fixed rate.", "C. The difference between a fixed and floating rate.", "D. The average of fixed and floating rates."]
],
"answers": [
    "C. Zero.",
    "B. By the current spot price minus the present value of the forward contract price.",
    "A. By the spot price minus the forward price.",
    "C. The forward seller has an equal loss.",
    "A. The security that determines the value of a derivative security.",
    "D. The liquidity and regulation.",
    "A. A floating rate."
],
  "references": [
    "Page 31",
    "Page 31",
    "Page 31",
    "Page 31",
    "Page 1",
    "Page 8",
    "Page 40"
  ]
},
            "Pricing and Valuation of Futures Contracts": {
  "questions": [
    "How does the price of a forward contract behave over its life when no mark-to-market gains or losses are paid?",
    "How does the value of a futures contract change with daily mark-to-market payments?",
    "How is the futures price of an interest rate stated in terms of the market reference rate from time A to time B?",
    "What is the primary difference between the value of a forward contract and a futures contract?",
    "For which type of contract are daily mark-to-market gains and losses settled?",
    "If interest rates are constant or uncorrelated with futures prices over time, how do the prices of futures and forwards compare?",
    "What is the primary distinction between futures and forwards for pricing?"
  ],
"choices": [
    ["A. It remains constant.", "B. It fluctuates with changes in the underlying value.", "C. It adjusts to the settlement price daily.", "D. It is reset based on the spot price of the underlying."],
    ["A. It remains constant.", "B. It fluctuates with changes in the underlying value.", "C. It adjusts to the settlement price daily.", "D. It is reset based on the spot price of the underlying."],
    ["A. futures price = 100 × MRRA, B–A", "B. futures price = MRRA, B–A", "C. futures price = 100 – (100 × MRRA, B–A)", "D. futures price = 100 + (100 × MRRA, B–A)"],
    ["A. The forward contract's value remains constant, while the futures contract's value fluctuates.", "B. The forward contract's value fluctuates, while the futures contract's value remains constant.", "C. The forward contract's value and futures contract's value both remain constant.", "D. The forward contract's value and futures contract's value both fluctuate."],
    ["A. Only for forward contracts.", "B. Only for futures contracts.", "C. For both forward and futures contracts.", "D. Neither for forward nor for futures contracts."],
    ["A. Futures prices are higher than forwards prices.", "B. Forwards prices are higher than futures prices.", "C. The prices of futures and forwards are the same.", "D. The prices of futures and forwards cannot be compared."],
    ["A. The underlying asset.", "B. The contract size.", "C. The settlement date.", "D. The daily mark-to-market gains and losses."]
],
"answers": [
    "A. It remains constant.",
    "C. It adjusts to the settlement price daily.",
    "C. futures price = 100 – (100 × MRRA, B–A)",
    "B. The forward contract's value fluctuates, while the futures contract's value remains constant.",
    "B. Only for futures contracts.",
    "C. The prices of futures and forwards are the same.",
    "D. The daily mark-to-market gains and losses."
],
  "references": [
    "Page 36",
    "Page 36",
    "Page 36",
    "Page 36",
    "Page 36",
    "Page 38",
    "Page 37"
  ]
},
            "Pricing and Valuation of Interest Rates and Other Swaps": {
  "questions": [
    "In a simple fixed-for-floating interest rate swap, what does one party pay?",
    "At the inception of a swap, what is the value to each party?",
    "How is the fixed-rate payment in an interest rate swap calculated for a notional principal amount of $10 million and a fixed rate of 2% with quarterly payments?",
    "What is the primary difference between the price and value of a swap?",
    "Which of the following best describes the floating-rate receiver position in a fixed-for-floating interest-rate swap?",
    "At initiation, why does a swap have zero value?",
    "How can an interest-rate swap be described in terms of forward contracts?"
  ],
"choices": [
    ["A. A fixed rate on a notional principal amount.", "B. A floating rate on a notional principal amount.", "C. Both fixed and floating rates on a notional principal amount.", "D. Neither fixed nor floating rates."],
    ["A. Positive.", "B. Negative.", "C. Zero.", "D. Undefined."],
    ["A. $10 million × 0.02", "B. $10 million × 0.02/4", "C. $10 million × 0.02/12", "D. $10 million × 0.02/2"],
    ["A. The price is the fixed rate of interest specified in the swap contract, while the value depends on how expected future floating rates change over time.", "B. The price depends on how expected future floating rates change over time, while the value is the fixed rate of interest specified in the swap contract.", "C. Both price and value are the fixed rates of interest specified in the swap contract.", "D. Both price and value depend on how expected future floating rates change over time."],
    ["A. Buying a fixed-rate bond and a floating-rate note.", "B. Buying a floating-rate note and issuing a fixed-rate bond.", "C. Issuing a floating-rate note and buying a fixed-rate bond.", "D. Neither buying nor issuing any bonds."],
    ["A. Because the fixed-rate payments are higher than the floating-rate payments.", "B. Because the floating-rate payments are higher than the fixed-rate payments.", "C. Because the present value of the fixed-rate payments equals the present value of the expected floating-rate payments.", "D. Because the swap rate is set to a non-zero value."],
    ["A. As equivalent to a series of forward contracts based on a fixed rate of interest.", "B. As equivalent to a single forward contract based on a floating rate of interest.", "C. As equivalent to a series of forward contracts based on a floating rate of interest.", "D. As unrelated to any forward contracts."]
],
  "answers": [
    "A. A fixed rate on a notional principal amount.",
    "C. Zero.",
    "B. $10 million × 0.02/4",
    "A. The price is the fixed rate of interest specified in the swap contract, while the value depends on how expected future floating rates change over time.",
    "B. Buying a floating-rate note and issuing a fixed-rate bond.",
    "C. Because the present value of the fixed-rate payments equals the present value of the expected floating-rate payments.",
    "C. As equivalent to a series of forward contracts based on a floating rate of interest."
  ],
  "references": [
    "Page 40",
    "Page 10",
    "Page 10",
    "Page 41",
    "Page 42",
    "Page 41",
    "Page 41"
  ]
},
            "Pricing and Valuation of Options": {
  "questions": [
    "What does 'Moneyness' refer to in the context of options?",
    "When is a call option considered 'in-the-money'?",
    "What is the time value of an option?",
    "How does an increase in the risk-free rate affect call option values?",
    "Which factor determines the value of an option?",
    "What is the relationship between the price of the underlying asset and the value of a call option?",
    "When does the time value of an option become zero?"
  ],
"choices": [
    ["A. The time value of an option.", "B. Whether an option is in the money or out of the money.", "C. The exercise value of an option.", "D. The speculative value of an option."],
    ["A. When S − X > 0.", "B. When S − X < 0.", "C. When S = X.", "D. When the option's time value is positive."],
    ["A. The amount by which the option premium exceeds the exercise value.", "B. The value of the option if exercised immediately.", "C. The difference between the option's premium and its moneyness.", "D. The speculative value of the option."],
    ["A. Increases call option values.", "B. Decreases call option values.", "C. Has no effect on call option values.", "D. Makes call option values volatile."],
    ["A. The volatility of the underlying asset.", "B. The exercise price of the option.", "C. The risk-free rate of interest.", "D. All of the above."],
    ["A. The higher the price of the underlying, the greater the exercise value of the call option.", "B. The lower the price of the underlying, the greater the exercise value of the call option.", "C. The price of the underlying has no effect on the exercise value of the call option.", "D. The exercise value of the call option is always equal to the price of the underlying."],
    ["A. At the start of the option's life.", "B. When the option is out of the money.", "C. At expiration.", "D. When the option is in the money."]
],
  "answers": [
    "B. Whether an option is in the money or out of the money.",
    "A. When S − X > 0.",
    "A. The amount by which the option premium exceeds the exercise value.",
    "A. Increases call option values.",
    "D. All of the above.",
    "A. The higher the price of the underlying, the greater the exercise value of the call option.",
    "C. At expiration."
  ],
  "references": [
    "Page 44",
    "Page 44",
    "Page 45",
    "Page 49",
    "Page 49",
    "Page 49",
    "Page 50"
  ]
},
            "Option Replication Using Put–Call Parity": {
  "questions": [
    "What is a fiduciary call?",
    "What is the payoff for a protective put when the put is out of the money?",
    "For put-call parity, what should be equal for the exercise prices on the put and the call?",
    "If at expiration S is greater than or equal to X, what is the payoff for the fiduciary call?",
    "What is the payoff for a protective put when the put is in the money?",
    "In the context of put-call-forward parity, what is created by purchasing a pure discount bond and simultaneously taking a long position in the forward contract?",
  ],
"choices": [
    ["A. A combination of a call with exercise price X and a stock.", "B. A combination of a put with exercise price X and a stock.", "C. A combination of a call with exercise price X and a pure-discount, riskless bond that pays X at maturity.", "D. A combination of a put with exercise price X and a pure-discount, riskless bond that pays X at maturity."],
    ["A. X", "B. S", "C. X + S", "D. S - X"],
    ["A. The face value of the riskless bond.", "B. The current stock price.", "C. The forward contract price.", "D. The option premium."],
    ["A. S", "B. X", "C. S + X", "D. S - X"],
    ["A. X", "B. S", "C. X + S", "D. S - X"],
    ["A. A synthetic option.", "B. A synthetic asset.", "C. A synthetic bond.", "D. A synthetic stock."]
],
  "answers": [
    "C. A combination of a call with exercise price X and a pure-discount, riskless bond that pays X at maturity.",
    "B. S",
    "A. The face value of the riskless bond.",
    "A. S",
    "A. X",
    "B. A synthetic asset.",
  ],
  "references": [
    "\"A fiduciary call is a combination of a call with exercise price X and a pure-discount, riskless bond that pays X at maturity (option expiration).\" - **Page 52**",
    "\"The expiration date payoff for a protective put is ... S when the put is out of the money.\" - **Page 52**",
    "\"When working with put-call parity, it is important to note that the exercise prices on the put and the call and the face value of the riskless bond are all equal to X.\" - **Page 52**",
    "\"If at expiration S is greater than or equal to X: ... The fiduciary call pays X + (S − X) = S.\" - **Page 52**",
    "\"The expiration date payoff for a protective put is (X − S) + S = X when the put is in the money.\" - **Page 52**",
    "\"By purchasing such a pure discount bond and simultaneously taking a long position in the forward contract, an investor has created a synthetic asset.\" - **Page 54**",
  ]
},
            "Valuing a Derivative Using a One-Period Binomial Model": {
  "questions": [
    "What is the primary concept behind a binomial model?",
    "In a one-period binomial model, which of the following is NOT required?",
    "What is the significance of risk-neutral probabilities in a one-period binomial model?",
    "In a one-period binomial model, how is the value of an option described based on risk neutrality?",
    "Why are risk-neutral probabilities used in a one-period binomial model for option pricing?",
    "What is the hedge ratio in the context of a one-period binomial model?",
    "In a one-period binomial model, how is the value of an option determined using the concept of risk neutrality?"
  ],
"choices": [
    ["A. The value will change to one of three possible values.", "B. The value will change to one of two possible values.", "C. The value remains constant over the period.", "D. The value will change based on a continuous distribution."],
    ["A. An exercise price for the option.", "B. Returns that result from an up-move and a down-move.", "C. The risk-free rate over the period.", "D. The volatility of the underlying asset."],
    ["A. They represent the actual probabilities of up- and down-moves.", "B. They are derived from historical data.", "C. They come from constructing a hedge that creates a certain payoff.", "D. They are used to adjust the risk-free rate."],
    ["A. The present value of a probability-weighted average of three possible outcomes.", "B. The present value of a probability-weighted average of two possible outcomes.", "C. The future value of a probability-weighted average of two possible outcomes.", "D. The future value of a probability-weighted average of three possible outcomes."],
    ["A. They are unbiased estimators of the actual probabilities.", "B. The model is based on a no-arbitrage relationship.", "C. They maximize the option's value.", "D. The buyer can let an out-of-the-money option expire unexercised."],
    ["A. The ratio of the option's value to the underlying asset's value.", "B. The number of shares of the underlying required to construct portfolios with certain payoffs.", "C. The ratio of the risk-free rate to the option's value.", "D. The ratio of the option's exercise price to its market price."],
    ["A. By calculating its payoffs for both an up-move and a down-move, then calculating the expected payoff as a weighted average using the risk-neutral probabilities, and finally discounting this expected payoff for one period at the risk-free rate.", "B. By using historical data to estimate the option's future value.", "C. By using the Black-Scholes model.", "D. By using the actual probabilities of up- and down-moves."]
],
  "answers": ["B", "D", "C", "B", "B", "B", "A"],
  "references": [
    "\"Recall from Quantitative Methods that a binomial model is based on the idea that, over the next period, some value will change to one of two possible values (binomial).\" - **Page 56**",
    "\"To construct a one-period binomial model for pricing an option, we need: A value for the underlying at the beginning of the period, An exercise price for the option, Returns that will result from an up-move and a down-move, The risk-free rate over the period.\" - **Page 56**",
    "\"Note that the actual probabilities of an up-move and a down-move do not enter directly into our calculation of option value. The size of the up-move and down-move, along with the risk-free rate, determines the risk-neutral probabilities we use to calculate the expected payoff at option expiration.\" - **Page 60**",
    "\"In a one-period binomial model based on risk neutrality, the value of an option is best described as the present value of a probability-weighted average of two possible outcomes.\" - **Page 60**",
    "\"A one-period binomial model for option pricing uses risk-neutral probabilities because the model is based on a no-arbitrage relationship.\" - **Page 60**",
    "\"The number of units of the underlying required to construct such portfolios is the hedge ratio.\" - **Page 60**",
    "\"To determine the value of an option using the concept of risk neutrality, we calculate its payoffs for both an up-move and a down-move, calculate the expected payoff as a weighted average using the risk-neutral probabilities of an up-move and a down-move, and discount this expected payoff for one period at the risk-free rate.\" - **Page 60**"
  ]
}
       },
        "ETHICAL AND PROFESSIONAL STANDARDS":{
            "Ethics and Trust in the Investment Profession": {
    "questions": [
        "Question 1: How can ethics be described?",
        "Question 2: What is the role of a code of ethics in defining a profession?",
        "Question 3: Which of the following is NOT a characteristic of a profession?",
        "Question 4: Why are high ethical standards particularly important in investment management?",
        "Question 5: What does a fiduciary standard require professionals to do?",
        "Question 6: What is one of the challenges to ethical behavior?",
        "Question 7: Why is trust in investment professionals of greater importance than in many other businesses?"
    ],
    "choices": [
        ["A. A set of shared beliefs about what is good or acceptable behavior.", "B. A written set of moral principles.", "C. A guideline for professional conduct.", "D. A regulatory body to enforce rules."],
        ["A. To communicate the values and expectations of an organization.", "B. To enforce rules concerning professional behavior.", "C. To monitor the ethical behavior of members.", "D. To provide a general guide to what constitutes acceptable behavior."],
        ["A. A focus on service to society.", "B. A requirement to put client interests first.", "C. A focus on profit maximization.", "D. A focus on the needs of their clients."],
        ["A. Because investment advice is a tangible product.", "B. Because clients often have significant knowledge about financial securities.", "C. Because investment professionals are entrusted with their clients’ wealth.", "D. Because ethical standards increase the cost of raising capital."],
        ["A. Match client return requirements with the characteristics of the securities.", "B. Act in the best interests of the client.", "C. Monitor the ethical behavior of members.", "D. Provide clients with information on laws and regulations."],
        ["A. Underestimating one’s own ethical character.", "B. Overestimating the importance of a code of ethics.", "C. Ignoring the needs of stakeholders.", "D. Avoiding the use of a decision-making framework."],
        ["A. Because investment advice is a tangible product.", "B. Because investment professionals handle tangible assets.", "C. Because investment advice and management are intangible products.", "D. Because trust is not essential in other businesses."]
    ],
    "answers": [
        "A. A set of shared beliefs about what is good or acceptable behavior.",
        "D. To provide a general guide to what constitutes acceptable behavior.",
        "C. A focus on profit maximization.",
        "C. Because investment professionals are entrusted with their clients’ wealth.",
        "B. Act in the best interests of the client.",
        "A. Underestimating one’s own ethical character.",
        "C. Because investment advice and management are intangible products."
    ],
    "references": [
        "Reference: \"Ethics can be described as a set of shared beliefs about what is good or acceptable behavior and what is bad or unacceptable behavior.\" - Page 1",
        "Reference: \"Having a code of ethics is a way to communicate the values, principles, and expectations of an organization or other group of people and provides a general guide to what constitutes acceptable behavior.\" - Page 1",
        "Reference: \"A profession is an occupational group ... A requirement to put client interests first.\" - Page 2",
        "Reference: \"Investment professionals have a special responsibility because they are entrusted with their clients’ wealth.\" - Page 2",
        "Reference: \"A fiduciary standard is stronger, requiring professionals to use their knowledge and expertise to act in the best interests of the client.\" - Page 3",
        "Reference: \"Challenges to ethical behavior include overestimating one’s own ethical character,\" - Page 6",
        "Reference: \"Investment advice and management are intangible products, making quality and value received more difficult to evaluate than for tangible products such as a laptop computer or a restaurant meal.\" - Page 2"
    ]
    },  
            "Code of Ethics and Standards of Professional Conduct": {
 "questions": [
   "What is the purpose of a professional code of ethics?",
   "What does a profession refer to?",
   "What is the role of the CFA Institute Professional Conduct Program?",
   "Which of the following is NOT a circumstance that can prompt an inquiry by the CFA Institute Professional Conduct staff?",
   "What is the primary objective of ethical behavior?",
   "Which standard relates to additional compensation arrangements?",
   "What is the responsibility of investment professionals?"
 ],
"choices": [
    ["A. To guarantee that all members will always follow the code.", "B. To communicate the values, principles, and expectations of an organization.", "C. To provide a detailed list of all acceptable behaviors."],
    ["A. A group of people with any skills.", "B. A group of people with specialized skills and knowledge who serve others.", "C. A group of people who follow a specific code of conduct."],
    ["A. To provide training to members.", "B. To enforce the Code and Standards.", "C. To conduct annual meetings."],
    ["A. Self-disclosure by members on their annual Professional Conduct Statements.", "B. Receiving a gift from a client.", "C. Evidence of misconduct by a member received through public sources."],
    ["A. To ensure personal benefits.", "B. To conform to a set of rules and moral principles.", "C. To achieve professional recognition."],
    ["A. Standard I: Professionalism", "B. Standard II: Integrity of Capital Markets", "C. Standard IV: Duties to Employers"],
    ["A. To ensure maximum profits at any cost.", "B. To use their specialized knowledge and skills to protect and grow client assets.", "C. To always choose the best investment options available."]
],
 "answers": ["B", "B", "B", "B", "B", "C", "B"],
 "references": [
   "A code of ethics is a written set of moral principles that can guide behavior by describing what is considered acceptable behavior.",
   "A profession refers to a group of people with specialized skills and knowledge who serve others and agree to behave in accordance with a code of ethics.",
   "The CFA Institute Board of Governors has overall responsibility for the Professional Conduct Program and its Disciplinary Review Committee is responsible for enforcing of the Code and Standards.",
   "The CFA Institute Professional Conduct staff conducts inquiries related to professional conduct. Several circumstances can prompt such an inquiry...",
   "Ethical behavior is that which conforms to a set of rules and moral principles based on shared beliefs about what behavior is acceptable and what behavior is unacceptable.",
   "The standard related to additional compensation arrangements is a subsection of Standard IV Duties to Employers.",
   "Investment professionals have a special responsibility to use their specialized knowledge and skills to both protect and grow client assets."
 ]
},
            "Guidance for Standards I–VII": {
 "questions": [
   "What should members provide their employers with at least?",
   "What must Members and Candidates not engage in regarding CFA Institute Programs?",
   "What is considered a violation regarding the integrity of the CFA charter?",
   "What must Members and Candidates ensure when communicating investment performance information?",
   "What is strictly prohibited in professional conduct?",
   "What is the guidance regarding settling disputes related to professional ethics or competence?",
   "What is considered \"material\" information?",
   "What is a violation of Standard II(A) Material Nonpublic Information?",
   "What is considered a violation regarding market participants?",
   "What is the guidance for firms regarding unethical behavior?"
 ],
"choices": [
    ["A. Monthly updates", "B. Biannual updates", "C. Quarterly updates"],
    ["A. Any conduct that promotes CFA Institute.", "B. Any conduct that compromises the reputation or integrity of CFA Institute.", "C. Any conduct that supports other competing designations."],
    ["A. Discussing the CFA curriculum.", "B. Cheating on the CFA exam.", "C. Attending CFA workshops."],
    ["A. That it is detailed and lengthy.", "B. That it is fair, accurate, and complete.", "C. That it is only positive."],
    ["A. Honest disagreements.", "B. Dishonesty, fraud, or deceit.", "C. Professional debates."],
    ["A. Members can use enforcement of the Standard against another member.", "B. Members must not use enforcement of the Standard against another member to settle personal disputes.", "C. Members should always involve third-party mediators."],
    ["A. Information that is commonly known.", "B. Information that would affect the price of a security.", "C. Information that is irrelevant to investors."],
    ["A. Sharing public information.", "B. Acting on material nonpublic information.", "C. Discussing public financial reports."],
    ["A. Making trades based on public information.", "B. Making trades intended to mislead market participants.", "C. Making trades based on personal preferences."],
    ["A. Encourage unethical behavior for profits.", "B. Ignore unethical behavior.", "C. Make clear that unethical behavior will not be tolerated."]
],
 "answers": ["C", "B", "B", "B", "B", "B", "B", "B", "B", "C"],
 "references": [
   "Members should provide their employers with updates at least quarterly.",
   "Members and Candidates must not engage in any conduct that compromises the reputation or integrity of CFA Institute or the CFA designation or the integrity, validity, or security of CFA Institute programs.",
   "Cheating on the CFA exam or any exam.",
   "When communicating investment performance information, Members and Candidates must make reasonable efforts to ensure that it is fair, accurate, and complete.",
   "Members and Candidates must not engage in any professional conduct involving dishonesty, fraud, or deceit.",
   "The guidance states, in fact, that members must not try to use enforcement of this Standard against another member to settle personal, political, or other disputes that are not related to professional ethics or competence.",
   "Information is “material” if its disclosure would affect the price of a security or if a reasonable investor would want the information before making an investment.",
   "Members and Candidates who possess material nonpublic information that could affect the value of an investment must not act or cause others to act on the information.",
   "Of course, spreading false information to affect prices or volume is a violation of this Standard as is making trades intended to mislead market participants.",
   "Develop and adopt a code of ethics and make clear that unethical behavior will not be tolerated."
 ]
},
            "Introduction to the Global Investment Performance Standards (GIPS)": {
 "questions": [
   "Why were the GIPS standards created?",
   "Who can claim compliance with GIPS?",
   "What is one of the biases that firms might have when choosing their own methodologies for reporting?",
   "What does GIPS compliance ensure regarding terminated accounts?",
   "What is the purpose of independent verification in GIPS compliance?",
   "Who should perform the independent verification for GIPS compliance?",
   "What should firms avoid in their performance reporting to prevent misrepresentation?"
 ],
"choices": [
    ["A. To allow firms to choose their own methodologies.", "B. To make investment performance reporting standardized and comparable across firms.", "C. To highlight top-performing portfolios only."],
    ["A. Any firm, including software developers.", "B. Only firms that manage assets for others.", "C. Consultants who serve their existing and prospective clients."],
    ["A. Reporting only during economic downturns.", "B. Including all accounts, regardless of performance.", "C. Excluding terminated accounts."],
    ["A. They should be excluded from all reports.", "B. They should be highlighted separately.", "C. They should be included in the composite."],
    ["A. To allow firms to self-verify their compliance.", "B. To ensure that a firm's performance measurement practices and methods are in line with GIPS.", "C. To highlight the top-performing portfolios."],
    ["A. The firm itself.", "B. A third party.", "C. Any individual within the firm."],
    ["A. Including all accounts.", "B. Reporting performance during economic upturns.", "C. Selecting specific time periods that showcase their performance in the best light."]
],
 "answers": ["B", "B", "C", "C", "B", "B", "C"],
 "references": [
   "GIPS present a standardized methodology for performance reporting that makes comparison of performance across firms meaningful...",
   "GIPS only apply to firms that manage assets for others.",
   "Excluding terminated accounts, which may tend to be accounts closed by investors due to sub-par performance.",
   "A GIPS-compliant composite must include terminated accounts.",
   "Firms are encouraged to pursue independent verification of their compliance with GIPS. Verification applies to the entire firm’s performance measurement practices and methods...",
   "If a firm chooses to pursue verification, it must be performed by a third party, not by the firm itself...",
   "Selecting time periods to report that put firm performance in the best possible light."
 ]
},
            "Ethics Application": {
 "questions": [
   "What is the ethical consideration when a member discovers that their firm is overcharging clients?",
   "What is the violation when a member fails to investigate transactions in an account that appear to be at high risk?",
   "What is the ethical violation when a member forges customer signatures?",
   "What is the ethical concern when a member contributes to a politician’s campaign expecting preferential treatment?",
   "What does ethical conduct improve outcomes for?",
   "What is a key component of ethical conduct?",
   "What is the purpose of a code of ethics?"
 ],
"choices": [
    ["A. The member should ignore the situation.", "B. The member should report only to the clients.", "C. The member must disassociate from the activity and not work with any clients who are still being overcharged."],
    ["A. Not adhering to company policies.", "B. Violating money-laundering laws.", "C. Not updating client records."],
    ["A. Expediency.", "B. Misrepresentation.", "C. Independence and Objectivity."],
    ["A. Seeking public recognition.", "B. Expecting preferential treatment for receiving management contracts.", "C. Supporting political ideologies."],
    ["A. Only the individual.", "B. Stakeholders.", "C. Only the company."],
    ["A. Following personal beliefs.", "B. Balancing self-interest with the impact on others.", "C. Prioritizing self-interest above all."],
    ["A. To provide a general guide to what constitutes acceptable behavior.", "B. To list out company policies.", "C. To highlight individual achievements."]
],
 "answers": ["C", "B", "A", "B", "B", "B", "A"],
 "references": [
   "A member reports to his supervisor that their firm is overcharging clients... The member must disassociate from the activity and not work with any clients who are still being overcharged.",
   "A member violates the Standard by failing to investigate transactions in an account that appear to be at high risk of violating money-laundering laws...",
   "A member violates the Standards (and the law) by forging customer signatures for expediency.",
   "A member violates the Standard by contributing to a politician’s campaign, believing that it may lead to preferential treatment with regard to receiving management contracts for government pension fund money.",
   "Ethical conduct has been described as behavior that improves outcomes for stakeholders...",
   "Ethical conduct is behavior that balances your self-interest with the impact on others.",
   "A code of ethics is a written set of moral principles that can guide behavior by describing what is considered acceptable behavior."
 ]
}
        },    
        "PORTFOLIO MANAGEMENT (PART TWO)":{
            "Portfolio Management: An Overview": {
 "questions": [
   "What does the portfolio perspective refer to?",
   "What is the primary benefit of diversification in a portfolio?",
   "What are the three major steps in the portfolio management process?",
   "What is the starting point of the portfolio management process?",
   "What does the investment policy statement (IPS) detail?",
   "During which step does a portfolio manager examine current economic conditions to identify the most attractive asset classes?",
   "What is the primary purpose of the feedback step in the portfolio management process?"
 ],
"choices": [
    ["A. Evaluating investments based on individual performance.", "B. Evaluating individual investments by their contribution to the risk and return of an investor’s portfolio.", "C. Holding all wealth in a single stock."],
    ["A. It guarantees higher returns.", "B. It allows an investor to reduce portfolio risk without necessarily reducing the portfolio’s expected return.", "C. It ensures that all investments will perform well."],
    ["A. Planning, Execution, and Feedback.", "B. Analysis, Investment, and Review.", "C. Allocation, Diversification, and Monitoring."],
    ["A. Execution.", "B. Feedback.", "C. Planning."],
    ["A. Only the investor's return objectives.", "B. The investor’s investment objectives and constraints.", "C. The portfolio's past performance."],
    ["A. Planning.", "B. Execution.", "C. Feedback."],
    ["A. To analyze the investor's risk tolerance.", "B. To determine asset class allocations.", "C. To monitor changes and rebalance the portfolio periodically."]
],
 "answers": ["B", "B", "A", "C", "B", "B", "C"],
 "references": [
   "The portfolio perspective refers to evaluating individual investments by their contribution to the risk and return of an investor’s portfolio.",
   "Diversification allows an investor to reduce portfolio risk without necessarily reducing the portfolio’s expected return.",
   "There are three major steps in the portfolio management process: Step 1: The planning step... Step 2: The execution step... Step 3: The feedback step...",
   "Step 1: The planning step begins with an analysis of the investor’s risk tolerance, return objectives, time horizon, tax exposure, liquidity needs, income needs, and any unique circumstances or investor preferences.",
   "This analysis results in an investment policy statement (IPS) that details the investor’s investment objectives and constraints.",
   "Step 2: The execution step involves an analysis of the risk and return characteristics of various asset classes... a portfolio manager will examine current economic conditions...",
   "Step 3: The feedback step is the final step. Over time, investor circumstances will change... The portfolio manager must monitor these changes and rebalance the portfolio periodically..."
 ]
},
            "Basics of Portfolio Planning and Construction": {
 "questions": [
   "Why is a written investment policy statement (IPS) essential for an investment manager?",
   "What should the investor’s goals in terms of risk and return be determined as?",
   "Which of the following is NOT a major component of an IPS?",
   "What does tactical asset allocation focus on?",
   "How might imposing portfolio constraints based on ESG factors affect performance?",
   "For active ownership, what is crucial to clarify regarding investors and shares?",
   "What does the strategic asset allocation provide for a portfolio?"
 ],
"choices": [
    ["A. To ensure high returns for the client.", "B. To understand the client’s needs, circumstances, and constraints.", "C. To showcase the manager's expertise."],
    ["A. Mutually inclusive.", "B. Mutually exclusive.", "C. Independent of each other."],
    ["A. Description of Client circumstances.", "B. Investment Guidelines.", "C. Portfolio's past performance."],
    ["A. Long-term investment opportunities.", "B. Shorter-term opportunities in specific asset classes.", "C. Maintaining a fixed asset allocation."],
    ["A. It will always increase returns.", "B. It may decrease or increase returns.", "C. It has no impact on returns."],
    ["A. Whether investors intend to sell their shares.", "B. Whether investors intend to vote their shares themselves or direct managers to vote according to specified ESG factors.", "C. Whether investors prefer dividends or capital gains."],
    ["A. Short-term investment opportunities.", "B. The basic structure of a portfolio.", "C. Tactical deviations from the baseline."]
],
 "answers": ["B", "B", "C", "B", "B", "B", "B"],
 "references": [
   "An investment manager is very unlikely to produce a good result for a client without understanding that client’s needs, circumstances, and constraints.",
   "These should be determined jointly, as the goals of high returns and low risk (while quite popular) are likely to be mutually exclusive in practice.",
   "The major components of an IPS typically address the following: Description of Client circumstances, situation, and investment objectives... Investment Guidelines such as how the policy will be executed, asset types permitted, and leverage to be used.",
   "Tactical asset allocation refers to an allocation that deviates from the baseline (strategic) allocation in order to profit from a forecast of shorter-term opportunities in specific asset classes.",
   "Imposing portfolio constraints based on ESG factors may affect performance. Limiting the universe of investment choices may decrease returns, but good corporate governance and low ESG-related risks may increase returns.",
   "For active ownership, it is important to clarify whether investors intend to vote their shares themselves or direct managers to vote the shares according to specified ESG factors.",
   "The strategic asset allocation provides the basic structure of a portfolio."
 ]
},
            "The Behavioral Biases of Individuals": {
 "questions": [
   "What does traditional finance assume about individuals?",
   "What are cognitive errors primarily due to?",
   "What is the nature of emotional biases?",
   "Which bias occurs when individuals rationally form an initial view but then fail to change that view as new information becomes available?",
   "Which bias leads individuals to underestimate uncertainty and the standard deviation of their predictions?",
   "Which bias involves individuals placing a higher value on assets they own than if they did not own those same assets?",
   "What does the term cognitive dissonance refer to?",
   "Which bias is exhibited when participants go with the consensus or popular opinion?",
   "Which bias occurs when individuals give themselves credit for choosing profitable stocks in a bull market?",
   "Which bias may lead investors to ignore or misinterpret new information suggesting that valuations will not continue to rise?"
 ],
"choices": [
    ["A. Individuals act on emotions.", "B. Individuals act as perfectly rational economic beings.", "C. Individuals always make biased decisions."],
    ["A. Feelings and impulses.", "B. Faulty reasoning or irrationality.", "C. External influences."],
    ["A. They are related to conscious thought.", "B. They stem from feelings, impulses, or intuition.", "C. They arise from logical reasoning."],
    ["A. Confirmation bias.", "B. Representativeness bias.", "C. Conservatism bias."],
    ["A. Overconfidence bias.", "B. Hindsight bias.", "C. Anchoring bias."],
    ["A. Endowment bias.", "B. Regret-aversion bias.", "C. Status quo bias."],
    ["A. A situation where an individual holds conflicting beliefs.", "B. The inability to process information.", "C. The tendency to rely on emotions for decision-making."],
    ["A. Herding behavior.", "B. Confirmation bias.", "C. Representativeness bias."],
    ["A. Hindsight bias.", "B. Overconfidence bias.", "C. Confirmation bias."],
    ["A. Anchoring bias.", "B. Confirmation bias.", "C. Representativeness bias."]
],
 "answers": ["B", "B", "B", "C", "A", "A", "A", "A", "A", "B"],
 "references": [
   "Traditional finance assumes that individuals act as perfectly rational economic beings who objectively consider all relevant information to make rational decisions.",
   "Cognitive errors are due primarily to faulty reasoning or irrationality.",
   "Emotional biases are not related to conscious thought. Rather, they stem from feelings, impulses, or intuition.",
   "Conservatism bias occurs when market participants rationally form an initial view but then fail to change that view as new information becomes available.",
   "Prediction overconfidence leads individuals to underestimate uncertainty and the standard deviation of their predictions.",
   "This describes the endowment bias, where individuals place a higher value on assets they own than if they did not own those same assets.",
   "Psychologists use the term cognitive dissonance to refer to a situation where an individual holds conflicting beliefs or receives information that causes a current belief to be questioned.",
   "Herding behavior is a form of regret aversion where participants go with the consensus or popular opinion.",
   "Persistently good results combined with self-attribution bias can fuel overconfidence, as can hindsight bias (as investors give themselves credit for choosing profitable stocks in a bull market).",
   "Confirmation bias may lead investors to ignore or misinterpret new information suggesting that valuations will not continue to rise."
 ]
},
            "Introduction to Risk Management": {
 "questions": [
   "What are the primary objectives of the risk management process?",
   "What does risk management not seek to do?",
   "What does risk governance refer to?",
   "Which of the following is a component of an overall risk management framework?",
   "What does risk management aim to achieve regarding the risks an organization faces?",
   "What is one way to approach the problem of quantifying operational risks for a single organization?",
   "Which of the following best describes the interactions among the various risks an organization faces?"
 ],
"choices": [
    ["A. Minimize or eliminate all risks.", "B. Identify the risk tolerance, measure organizational risks, and modify and monitor these risks.", "C. Maximize returns and minimize uncertainties."],
    ["A. Minimize or eliminate all risks.", "B. Identify and measure organizational risks.", "C. Modify and monitor risks."],
    ["A. The process of identifying and measuring risks.", "B. Senior management’s determination of the risk tolerance of the organization and oversight of the risk management function.", "C. The process of modifying and monitoring risks."],
    ["A. Establishing processes and policies for risk governance.", "B. Ignoring risks that are hard to quantify.", "C. Focusing solely on financial risks."],
    ["A. Eliminate all risks.", "B. Align the risks with its risk tolerances.", "C. Increase exposure to all risks."],
    ["A. Ignore the risk as it's too unpredictable.", "B. Examine a large sample of firms to determine the probability of significant losses.", "C. Rely solely on historical data of the organization."],
    ["A. Risks are independent and do not interact.", "B. Interactions among risks are rare and insignificant.", "C. Interactions among risks are many and frequent, especially during periods of stress in financial markets."]
],
 "answers": ["B", "A", "B", "A", "B", "B", "C"],
 "references": [
   "The risk management process seeks to (1) identify the risk tolerance of the organization, (2) identify and measure the risks that the organization faces, and (3) modify and monitor these risks.",
   "The process does not seek to minimize or eliminate all of these risks.",
   "Risk governance refers to senior management’s determination of the risk tolerance of the organization, the elements of its optimal risk exposure strategy, and the framework for oversight of the risk management function.",
   "An overall risk management framework encompasses several activities, including: Establishing processes and policies for risk governance.",
   "Through these choices the firm aligns the risks it takes with its risk tolerances for these various types of risk.",
   "One way to approach this problem is to examine a large sample of firms in order to determine an overall probability of significant losses due to operational risks and the average loss of firms that have experienced such losses.",
   "Interactions among risks must be considered because such interactions are many and frequent. They can be especially important during periods of stress in financial markets."
 ]
}
        }
                    }
    }

total_questions = 0
for reading, content in exams["CFA Level 1"]["PORTFOLIO MANAGEMENT (PART ONE)"].items():
    total_questions += len(content["questions"])

space = ("<p> </p>")

blue_line = ("""
        <style>
            @keyframes fadeInOut {
                0% {
                    opacity: 0;
                }
                50% {
                    opacity: 1;
                }
                100% {
                    opacity: 0;
                }
            }
            
            hr.customHR {
                border: none;
                border-top: 2px solid #335575;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                animation: fadeInOut 5s ease-in-out infinite;
            }
        </style>
        <hr class="customHR">
    """)
grey_line = ("""
        <style>
            @keyframes fadeInOut {
                0% {
                    opacity: 0;
                }
                50% {
                    opacity: 1;
                }
                100% {
                    opacity: 0;
                }
            }
            
            hr.customHR {
                border: none;
                border-top: 2px solid #4A4A4A ;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
                animation: fadeInOut 5s ease-in-out infinite;
            }
        </style>
        <hr class="customHR">
    """)

