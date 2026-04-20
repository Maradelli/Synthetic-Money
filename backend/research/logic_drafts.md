# Explanation of some decisions & Results
## 1. Choosing segments
### 1.1. Data & methods of its proccesing  
First of all, we need to define general categories and their distribution based on official statistics. All my research will be based on statistics of the Russian Federation because the application will be adapted to the russian market.

As we can see in file ***'CPR_Gr_Tov-RF_2026.xlsx'*** that was downloaded from the [Federal State Statistics Service](https://rosstat.gov.ru/statistics/price#), *39.002%* of expenses are food products, *32.772%* of expenses are non-food products, and *28.226%* of expenses are services.

![Pic. 1](image.png)

Now we need to get into the details of each category.
To group this data, I manually calculated ratio of each segment like that:

![Pic. 2](image-1.png)



### 1.2. Results

1. **Food** (30-35%). This group has the highest frequency and pretty low average cheque. Examples from this category: meat (8.821%), milk and dairy products (3.117%), pastry (2.693%), etc.
2. **Transport** (4-5%). This segment can be described as the group with high frequency and small sums. These are taxi, travel cards, etc. 
3. **Auto** (8-10%). This category can be described as the group with low frequency and high sums. Plus we should mention that there can be rare situations like an expensive repair so we'll have to count it later.     
4. **Housing and communal services** ($\approx$9.8%). This group has low frequency of expenses (once per month) and fixed sums.
5. **Communications** (3-4%). These are Wi-Fi, mobile internet, etc.
6. **Healthcare** (5-7%). This segment can be defined by unregular expenses and volatile cheque.
7. **Clothing and shoes** (8-10%). This category has seasonal spikes. Also there are high volatility, for example, one T-shirt can cost 500 rubles and the other one with famous logo can cost up to 150 000 rubles.
8. **Restaurants & cafe** (5-7%). This group has significant correlation with weekends and holidays.
9. **Entertainment** (3-4%). There is high concentration of anomalies what can be described as high but rare expenses.
10. **Other** (12-17%). This category can be described as the 'Long Tail' of the distribution.

## 2. Distribution
### 2.1. Amount distribution
In this section we need to define a lot of details for different distributions to create a general model based on statistics and probability theory.

First of all, we need to understand what the type of our general distribution is. For that purpose we can find some facts about our 'real' data:
1. **Transactions cannot be negative**. There's no way to send -1500 rubles from one account to another so from the point of the mathematics it will look like that: 

    $X \in [0; +\infin]$, where $X$ - amount (rubles)    
2. **Skewness**. Most of cheques lay around the mean value but there are some expenses placed far away to the right side from the mean value. This distribution looks like that:

![Pic.3](the-long-tail.jpg)

Based on these facts, we can use for modeling most of our data **log-normal distribution (PDF)**:

$$\boxed{f(x)=\frac{1}{x\sigma\sqrt{2\pi}}exp(-\frac{(lnx - \mu)^2}{2\sigma^2})}$$, where 

- $\sigma$ - standard deviation of the variable's natural logarithm ($lnX$), 

- $\mu$ - expected value (mean) of the variable's natural logarithm ($lnX$)

***
Now we need to find our real distribution. You can see the process of calculating parameters lower for each category. But before that we should mention what we'll check our calculations by next formula: $\boxed{Median = e^\mu}$.

Also I would like to mention that some numbers will be chosen only by logical sense because the lack of information.

1. **Food**. As declared on this [website](https://www.rsb.ru/press-center/publications/2025/291225/) of one of Russian's bank $E$ = **809** rubles, $max$ = **852** rubles, $min$ = **780** rubles. Let's calculate our parameters:

    $\sigma_f = \frac{ln(max) - ln(min)}{6} = \frac{ln(852) - ln(780)}{6} \approx$ **0.147**

    $\mu_f = ln(E) - \frac{\sigma_f^2}{2} \approx 6.696 - 0.011$ = **6.685**

    $Median_f = e^{6.685} \approx$ **800.31** rubles $\to$ calculations are __correct__.
2. **Auto**. As said on the [website](https://www.banki.ru/news/daytheme/?id=11020468) $E$ = **15000** rubles, $max$ = **97000** rubles, $min$ = **10000** rubles:

    $\sigma_A = \frac{ln(max) - ln(min)}{6} = \frac{ln(97000) - ln(10000)}{6} \approx$ **0.379**

    $\mu_A = ln(E) - \frac{\sigma_A^2}{2} \approx 9.616 - 0.072 =$ **9.544**

    $Median_A = e^{9.544} \approx$ **13960.68** rubles $\to$ calculations are __correct__.
3. **Transport**. I've got some problems with this category because there are not that many researches and statistics about public transport in public sources so I'll use this [website](https://finance.mail.ru/article/issledovanie-muzhchiny-chasche-pokupayut-aviabilety-a-zhenschiny-oplachivayut-taksi-63512180/) to approximate these parameters:

    For the last 2 years inflation in the Russian Federation was about **17.52**% so we should multiply our average value by 1.1752. Also there is another problem with prices for the taxi ($\approx$511 rubles) and public transport ($\approx$121 rubles) so we'll calculate our expected value as

    $E = \frac{511+121}{2} =$ **316** rubles, $max$ = **19376** rubles, $min$ = **121** rubles.
    
    $\sigma_T = \frac{ln(max) - ln(min)}{6} = \frac{ln(19376) - ln(121)}{6} \approx$ **0.846**

    $\mu_T = ln(E) - \frac{\sigma_T^2}{2} \approx 5.756 - 0.356 =$ **5.4**

    $Median_T = e^{5.4} \approx$ **221.41** rubles $\to$ calculations are __correct__.
4. **Housing and communal services**. There is the same problem as with the previous group about lack of public information so I'll use this [website](https://t-j.ru/zakroy-vodu-stat-2025/?utm_referrer=https%3A%2F%2Fyandex.ru%2F) for calculating our parameters:

    $E \approx$ **6800** rubles, $max$ = **10651** rubles, $min \approx$ **4000** rubles

    $\sigma_{HCS} = \frac{ln(max) - ln(min)}{6} = \frac{ln(10651)-ln(4000)}{6} \approx$ **0.163**

    $\mu_{HCS} = ln(E) - \frac{\sigma_{HCS}^2}{2} \approx 8.825 - 0.013 =$ **8.812**

    $Median_{HCS} = e^{8.812} \approx$ **6714.33** rubles $\to$ calculations are __correct__.
5. **Communications**. There are 2 different parts of this group with different behaviour: mobile internet and Wi-Fi. So that's the reason why exactly these values were chosen from this [website](https://3dnews.ru/1127889/kagdiy-rossiyanin-teper-tratit-na-mobilnuyu-svyaz-v-srednem-bolee-1100-rubley-v-mesyats):

    
    $E$ = **1100** rubles, $max$ = **3000** rubles, $min$ = **100** rubles. 

    $\sigma_T = \frac{ln(max) - ln(min)}{6} = \frac{ln(3000) - ln(100)}{6} \approx$ **0.567**

    $\mu_T = ln(E) - \frac{\sigma_T^2}{2} \approx 7.003 - 0.161 =$ **6.842**

    $Median_T = e^{6.842} \approx$ **936.36** rubles $\to$ calculations are __correct__. 
6. **Healthcare**. As declared on this [website](https://sberanalytics.ru/researches/year-results-health-expenses) of the biggest bank of the Russian Federation:

     $E$ = **1293** rubles - average value, $max$ = **8820** rubles, $min$ = **792** rubles.


    $\sigma_H = \frac{ln(max) - ln(min)}{6} = \frac{ln(8820) - ln(792)}{6}\approx$ **0.402**

    $\mu_H = ln(E) - \frac{\sigma_H^2}{2} \approx 7.165 - 0.081 =$ **7.084**

    $Median_H = e^{7.084} \approx$ **1192.73** rubles $\to$ calculations are __correct__.
7. **Clothing and shoes**. As declared on the same [website](https://sberanalytics.ru/researches/year-results-health-expenses) from point 3: 

    $E$ = **7196** rubles, $max$ = **8504** rubles, $min$ = **6738** rubles:

    $\sigma_{cl} = \frac{ln(max) - ln(min)}{6} = \frac{ln(8504) - ln(6738)}{6} \approx$ **0.039**

    $\mu_{cl} = ln(E) - \frac{\sigma_{cl}^2}{2} \approx 8.8813 - 0.0007 =$ **8.881**

    $Median_{cl} = e^{8.881} \approx$ **7193.98** rubles $\to$ calculations are __correct__.
8. **Restaraunts & cafe**. There is a lot of information about this category so we'll use information from this [website](https://www.banki.ru/news/lenta/?id=11021070):

    $E$ = **1300** rubles, $max$ = **5000** rubles, $min$ = **150** rubles.

    $\sigma_{RC} = \frac{ln(max)-ln(min)}{6} = \frac{ln(5000)-ln(150)}{6} \approx$ **0.584**

    $\mu_{RC} = ln(E) - \frac{\sigma_{RC}^2}{2} \approx 7.170 - 0.171 =$ **6.999**

    $Median_{RC} = e^{6.999} \approx$ **1095.54** rubles $\to$ calculations are __correct__.
9. **Entertainment**. We'll use information from this [website](https://www.kommersant.ru/doc/8315509):

    $E$ = **3000** rubles, $max$ = **10000** rubles, $min$ = **300** rubles.

    $\sigma_{E} = \frac{ln(max) - ln(min)}{6} = \frac{ln(10000) - ln(300)}{6} \approx$ **0.584**

    $\mu_{E} = ln(E) - \frac{\sigma_{E}^2}{2} \approx 8.006 - 0.171 =$ **7.835**

    $Median_E = e^{7.835} \approx$ **2527.54** rubles $\to$ calculations are __correct__.
10. **Other**. This category can be described as a total spending chaos because every amount which was not categorized as something else mentioned earlier will be here. So we'll have to choose all numbers without any source of information but our own logical sense:

    $E$ = **1500** rubles, $max$ = **20000** rubles, $min$ = **50** rubles.

    $\sigma_O = \frac{ln(max) - ln(min)}{6} = \frac{ln(20000) - ln(50)}{6} \approx$ **0.999**

    $\mu_O = ln(E) - \frac{\sigma_O^2}{2} \approx 7.313 - 0.499 =$ **6.814**

    $Median_O = e^{6.814} \approx$ **910.51** rubles $\to$ calculations are __correct__.
    
    High variance in __'Other'__ is designed to simulate rare large purchases (e.g. gadgets, home appliances) within a stream of small household expenses.
### 2.2. Seasonality & Intensity

Now we should discuss about seasonality and intensity because it's pretty obvious that we cannot make transactions every 5 seconds. So in this sectiong we'll find daily routine, weekly routine and monthly routine for each category mentioned earlier. 

To make our data more realistic let's create some categories of clients, their behaviour, and find weights for each category of transactions for them. For these purposes we'll use information from this [website](https://companies.rbc.ru/news/k2ORyiimZj/kakoj-u-vas-finansovyij-psihotip-i-kak-ego-skorrektirovat/). 

Let's define some variables: 

- $\Phi$ - coefficient of transaction's frequency

- $\alpha$ - coefficient of transaction's amount

The coefficient $\alpha$ actually 'shifts' the bell of the distribution to the right or left along the sum axis, and $\Phi$ changes the density of events on the timeline.
#### 2.2.1 Psychotypes & their behaviour
1. **The Goblin Treasurer**. This type of people cannot live without a thought about saving their own money at any cost. They're conservative and prefer to not borrow at all. They tries to minimize every unecessary expenses. So we've got the next picture of them:

    - $E$ gets closer to the $minimum$ for each category.
    - $Frequency$ will be $minimal$.
    - '**Other**' category will be almost equal to 0. However transactions in '**Restaraunts & cafe**' and '**Entertainment**' would happen at least once per month because of a 'special day', for example, birthday.

2. **The Party King**. These guys doesn't even think about their future. Their slogan is **to live today** so it's all says about their relationships with their money if they still have got one. This type can be described by these facts:
    - $E$ in '$Dining$' and '$Entertainment$' grows by __+40%__
    - A lot of small transactions in '$Food$' and '$Other$' categories
    - A spike of transactions in the first __3 days__ after payment then goes __'silence'__

3. **The Son of a mom's friend**. This is a perfect client's psychotype because they've got everything under their control: they don't spend any more or less that they need, their balance is always positive, they don't spend money impulsivly, etc. This type of people is really rare but their behaviour is the most predictable through all client's types:
    - Doesn't spend a lot of money on '$Other$' category
    - Investing in its own __health__ (attending doctors just for checkups)
    - Other transactions won't be changed by weights at all

4. **The Unstoppable Player**. We cannot certainly tell how much this type will spend tomorrow: 500 rubles or 500 000 rubles? There we'll see a huge __standard deviation__ in every category mentioned earlier:
    - Huge transactions in __'$Entertainment$'__ and __'$Other$'__ categories
    - There also will be chaotic transactions' behaviour in __'$Food$'__
    - Spends more money on __'$Restaurants$ & $cafe$'__ to celebrate its own successes

5. **The hypochondriac Survivalist**. These clients cares about safety of their money more than anything. They've got a permanent fear of staying without money, getting sick, losing their property, etc. Let's just describe them by next facts:
    - A lot of big transactions in __'$Health$'__
    - Always pays subscribes, utility bills, etc. __in time__
    - They barely go out because of the stress so their expenses in __'$Entertainment$'__ are low

So for we should update our formulas to include features of each category. In the code we'll use these formulas:
    
- $\boxed{Freq_{new} = Freq \cdot \Phi_i}$
- $\boxed{E_{new} = E \cdot \alpha_i}$
- $\boxed{\mu_{new} = ln(E_new) - \frac{\sigma^2}{2}}$
- where $i = \overline{1,5}$ - type of the psychotype 

There's the final table of coefficients for each type: (ADD)
#### 2.2.2 Daily & weekly routine
Let's define weights for a day and for a week. We need to do this because of peoples' different behaviour depending on the time of a day and the day of a week. For example, there will be more chance to have a spike of transactions in __'$Entertainment$'__ on Saturday than on Tuesday because most people work in the period between Monday and Friday what is called '5/2'.

We'll begin with a daily routine:

1) __00:00-06:00 - Sleep zone__. There will be the lowest amount of transactions (maybe some automatic subscriptions) because most people are asleep. The weight for this time will be equal to __0.1__.
2) __06:00-11:00 - Morning rush__. At that time people will be having breakfasts and their morning coffees, rushing to their jobs so the weight will be __0.7__.
3) __11:00-15:00 - Lunch time__. Active time for dining and small restaurant purchases. People often use this time for a break from work. The weight will be equal to __0.8__.
4) __15:00-18:00 - Afternoon lull__. Work focus increases, and transaction intensity drops slightly. The weight is __0.4__.
5) __18:00-22:00 - Evening peak__. The most active period when people buy groceries for dinner (__'$Food$'__), go to __'$Restaraunts$ & $cafe$'__, or enjoy __'$Entertainment$'__. The weight is __1.0__.
6) __22:00-00:00 - Late evening__. Transactions fade out as people prepare for sleep. Mostly online orders or late-night taxi rides. The weight is __0.2__.  

Now let's focus on a weekly routine:

1) __Monday-Thursday__. They are 'Working days' so here we can see a stable intensity with a focus on __'$Transport$'__ and __'$Food$'__.
2) __Friday__. Evening spike in __'$Restaurants$ & $cafe$'__ and __'$Entertainment$'__ categories.
3) __Saturday__. The absolute peak of the week. High intensity in __'$Clothing$ $and$ $shoes$'__, __'$Entertainment$'__, and large __'$Food$'__ purchases.
4) __Sunday__. Activity decreases toward the evening as people prepare for the new work week.

That's all information in this section that is needed for a future modeling.
#### 2.2.3 Monthly cycles
We can set two major inflow days: __the 10th__ and __25th__ of each month. During the 3 days following these dates, the transaction frequency coefficient $\Phi$ and the amount coefficient $\alpha$ will __increase by 20-30%__. For The Party King psychotype, this effect is maximized, leading to a 'spending spree' followed by a period of 'silence' when funds are exhausted. Also we should note that if the 10th is __Saturday__ then we'll use __the 9th__ of this month.

Certain categories don't follow a probability distribution but occur as fixed events:
- Housing and communal services (HCS): Typically one large transaction between __the 15th and 20th__ of the month.
- Communication services: A fixed payment for mobile and internet usually occurs on __the 1st day__ of the month or a __specific__ billing date.

### 2.3. Cross-Category Dependencies
In real life, transactions are rarely isolated events. They often form 'chains' or show inverse correlations. To make our generator indistinguishable from real banking data, we incorporate the following dependencies:
1) __Complementary dependencies__:
    - __Entertainment → Transport__: A high transaction in the __'$Entertainment$'__ category late in the evening (after 22:00) triggers a subsequent __'$Transport$'__ (taxi) transaction with a probability of __$\approx$0.8__.
    - __Auto → Other__: Maintenance in the __'$Auto$'__ category often correlates with __'$Other$'__ transactions (e.g., buying accessories or paying for parking).
2) __Substitution effect__:
    - __Food vs Restaurants & cafe__: These categories have an inverse relationship on a daily scale. If a user has a high-amount transaction in __'$Restaurants$ & $cafe$'__ (a family dinner), the probability of a __'$Food$'__ (grocery store) transaction on the same evening drops by __$\approx$60%__.
3) __Psychotype-Specific Chains__:
    - __The Unstoppable Player__: A successful "win" (modeled as a high __'$Other$'__ or __'$Entertainment$'__ transaction) triggers an immediate spree in __'$Restaurants$ & $cafe$'__ to celebrate.
    - __The hypochondriac Survivalist__: Large transactions in __'$Health$'__ (pharmacy/clinic) increase the probability of staying home, reducing __'$Transport$'__ and __'$Entertainment$'__ frequency to __near zero__ for the next 48 hours.

### 2.4. Fraud detection
To evaluate the effectiveness of anti-fraud systems, our generator must simulate not only legitimate behavior but also common fraudulent patterns. We will implement three main types of anomalies:
1) __Velocity attacks__:
    - __Logic__: A sudden burst of transactions in a very short period
    - __Simulation__: 10+ transactions within 60 seconds in categories like __'$Communications$'__ or __'$Other$'__ (e.g., small transfers or mobile top-ups to "clean" the card balance). Also we'll use __Poisson distribution__ with a very high value of $\lambda$ to simulate this scenario properly. In peaks $\lambda$ will be increased up to __50-100 times__.
2) __Account takeover | Behavioral Shift__:
    - __Logic__: Somehow client's card or account was stolen. For example, conservative __'Goblin Treasurer'__ suddenly starts spending like an __'Unstoppable Player'__.
    - __Simulation__: A sharp increase in $E$ and $\Phi$ coefficients for high-risk categories (__'$Entertainment$'__, __'$Other$'__) during unusual hours (e.g., the __'Sleep zone'__ 03:00 AM).
3) __Unusual location or merchants__:
    - __Logic__: Transactions from merchants that the user has never visited or that don't match their profile.
    - __Simulation__: Although our current dataset focus is on names, we will flag transactions as fraud if the __'Merchant_name'__ belongs to a __'high-risk' list__ that doesn't correlate with the Category or the user's typical daily route.