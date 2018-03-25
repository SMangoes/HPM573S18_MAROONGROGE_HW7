import SurvivalModelClasses as Cls
import scr.SamplePathClasses as SamplePathSupport
import scr.FigureSupport as Fig
from scipy.stats import binom

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

# plot the sample path
SamplePathSupport.graph_sample_path(
    sample_path=cohortOutcome.get_survival_curve(),
    title='Survival Curve',
    x_label='Time-Step (Year)',
    y_label='Number Survived')

# plot the histogram
Fig.graph_histogram(
    data=myCohort.get_survival_times(),
    title='Histogram of Patient Survival Time',
    x_label='Survival Time (Year)',
    y_label='Count')

# print the patient survival time
print('Average survival time (years):', cohortOutcome.get_ave_survival_time())
print('95% CI of average survival time (years)', cohortOutcome.get_CI_survival_time(ALPHA))

#Question 1
print('Question 1: 5 year survival (%)', cohortOutcome.get_5_yr_survival()*100)

#Question 2
print('Question 2: This would be a Binomial distribution, with n=N (number of pts in sample), and p=q (probability of survival past 5 years)')

#Question 3
print ('Question 3: The % chance we observe 400/573 patients surviving past 5 years if the true 5-year survival rate is 50% would be (in %)', 100* (binom.pmf(k=400,n=573,p=0.50)))

#Question 4
print ('Question 4: Estimate of mortality probability (95% credible interval): 0.0830 (0.0680, 0.1020)')

#Question 5
print ('Question 5: Mean survival time and 95% projection interval: 12.0200 (9.6910, 13.6270)')

#Question 6
print ('Question 6: Estimate of mortality probability (95% credible interval): 0.0837 (0.0720, 0.0965), Mean survival time and 95% projection interval: 12.0670 (10.4980, 13.4900), Compared with results in Q4 and Q5, the 95% credible interval is narrower, which is likely due to higher confidence in our calibrated results given the larger sample size'
       )
