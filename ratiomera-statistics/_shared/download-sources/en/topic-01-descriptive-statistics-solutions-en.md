---
title: "Complete Solutions"
subtitle: "Descriptive Statistics"
document-id: "topic-01-descriptive-statistics-solutions-en"
topic-id: "topic-01-descriptive-statistics"
topic-number: "01"
topic-slug: "descriptive-statistics"
document-type: "solutions"
locale: "en"
paired-document-id: "topic-01-descriptive-statistics-exercises-en"
---

These complete solutions use the same identifiers and order as the Exercise Sheet. Intermediate values are retained until the stated rounding step, so small differences caused by earlier rounding are acceptable where noted. All settings, values, data, and software outputs are constructed teaching material; they are not empirical findings.

# Part I: Theory

## A01: Deciding Whether a Mean Is Meaningful

### T01-A01-V01: Community-library variables

**Identify the issue**

Branch code is a nominal label, so its mean has no library meaning.

**Reason through the evidence**

Reading minutes are ratio-level and can be averaged; a median may better describe a skewed distribution.

The ordered service rating is ordinal, so category proportions, mode, and median are primary; a mean assumes equal category spacing.

**State the conclusion and its limits**

Fahrenheit temperature is interval-level, so its mean and differences are meaningful, although ratios are not.

Borrowed-item count is absolute, so a mean count is meaningful, with shape still relevant to representativeness.

### T01-A01-V02: Theater-festival records

**Identify the issue**

Ticket category is nominal, making a mean invalid.

Duration has a meaningful zero and equal units, so its mean is valid.

**Reason through the evidence**

Seat-row rank is ordinal; average ranks are sometimes compared under explicit conventions, but the median and distribution respect the guaranteed information.

Calendar year is interval-level, so an average year can summarize timing within a coherent set, not ratios of age.

**State the conclusion and its limits**

Curtain-call count is absolute and can be averaged.

Use the median alongside any mean when quantitative distributions are skewed.

### T01-A01-V03: Urban-garden observations

**Identify the issue**

Plot label is an identifier and remains nominal despite digits, so averaging it is meaningless.

**Reason through the evidence**

Soil moisture percentage is quantitative with equal intervals; within a common definition, a mean is meaningful, though a 0% reading needs physical interpretation before ratio claims.

Plant-health class is ordinal, so the median or category proportions are safer than a mean.

**State the conclusion and its limits**

Celsius temperature is interval-level and supports a mean but not temperature ratios.

Flowering-plant count is absolute and supports an average count.

### T01-A01-V04: Language-workshop data

**Identify the issue**

Badge number labels people and has no quantitative mean.

Practice hours have equal units and a meaningful zero, so averaging is defensible.

**Reason through the evidence**

Proficiency band is ordinal; a mean of arbitrary band codes assumes unsupported equal gaps.

A standardized fluency score is commonly treated as interval-level, allowing a mean while prohibiting literal ratio claims.

**State the conclusion and its limits**

Completed-module count is absolute and can be averaged.

In every quantitative case, inspect shape and missingness before calling the mean typical.

### T01-A01-V05: Public-transport records

**Identify the issue**

Route identifier is nominal.

Journey time is ratio-level, so a mean is valid but may be pulled upward by long delays.

**Reason through the evidence**

Satisfaction category is ordinal and is better summarized by proportions, mode, or median.

Clock time wraps after 24 hours; an ordinary mean can place late-night times at midday, so circular methods or a carefully chosen elapsed-time origin are needed.

**State the conclusion and its limits**

Transfer count is absolute and supports a mean.

Numeric appearance alone never licenses averaging.

### T01-A01-V06: Museum-collection fields

**Identify the issue**

Accession number is a nominal identifier and should not be averaged.

Object mass is ratio-level and supports a mean.

**Reason through the evidence**

Conservation-priority rank is ordinal, so its order is meaningful but equal rank gaps are not guaranteed.

Year created is interval-level on a common calendar; a mean year may summarize a coherent collection, while “twice as old” does not follow.

**State the conclusion and its limits**

Restoration count is absolute and can be averaged.

Distribution shape determines whether valid means are also representative.

### T01-A01-V07: Coastal-observation log

**Identify the issue**

Station name is nominal and has no mean.

**Reason through the evidence**

Wave height is ratio-level, so a mean is meaningful within a defined observation period.

Warning level is ordinal and favors category frequencies and a median.

**State the conclusion and its limits**

The local east-west coordinate is interval-level: a mean can locate a balance point within the fixed coordinate system, and coordinate differences are meaningful, but ratios depend on the arbitrary origin.

Seabird count is absolute and supports a mean count.

### T01-A01-V08: Digital-archive workflow

**Identify the issue**

File format is nominal, so only category summaries such as the mode apply.

Processing duration is ratio-level and may be averaged, with a median useful under right skew.

**Reason through the evidence**

Urgency rank is ordinal and does not guarantee equal gaps.

Time of day is circular: 23:55 and 00:05 are close, although their ordinary numeric mean is noon.

**State the conclusion and its limits**

Use circular summaries or elapsed time from a meaningful reference.

Page count is absolute and supports averaging.

### T01-A01-V09: Community-choir records

**Identify the issue**

Voice section is nominal and its mode, not a mean, identifies the most common category.

Attendance percentage has equal units and can be averaged when denominators and observation periods are comparable.

**Reason through the evidence**

Audition rank is ordinal and favors a median or rank distribution.

Frequency in hertz is ratio-level and has a meaningful arithmetic mean, although perceived pitch may motivate a logarithmic scale for another question.

**State the conclusion and its limits**

Missed-session count is absolute and can be averaged.

Codes and ranks do not become quantities merely because they use numerals.

### T01-A01-V10: Food-cooperative inventory

**Identify the issue**

Supplier ID is nominal, so its mean is meaningless.

Delivery mass is ratio-level and supports averaging.

**Reason through the evidence**

Freshness grade is ordinal, making a median, mode, and proportions defensible without assuming equal gaps.

Celsius storage temperature is interval-level, so a mean temperature is meaningful but “twice as warm” is not.

**State the conclusion and its limits**

Damaged-item count is absolute and supports a mean.

Equal numerical intervals support averaging; a label or order alone does not.

## A02: Measurement Levels, Including Numeric Identifiers

### T01-A02-V01: Variables in a neighborhood arts survey

**Identify the issue**

Mural ID is nominal: 4107 names a record, and another one-to-one code would preserve its meaning.

Preferred art form is also nominal.

**Reason through the evidence**

Juror placement is ordinal because order is meaningful but gaps between places are not fixed.

Celsius temperature is interval-level: differences survive a positive linear rescaling, but zero is conventional.

**State the conclusion and its limits**

Paint volume is ratio-level because equal units and a meaningful zero support ratios.

Submitted-design count is absolute because its natural unit is one design.

Averaging the ID would summarize the coding scheme, not murals.

### T01-A02-V02: Records from a public library

**Identify the issue**

Borrower code and book genre are nominal.

Damage condition is ordinal because its categories have rank but no guaranteed equal spacing.

**Reason through the evidence**

Publication year is interval-level on its calendar: differences are meaningful, whereas year ratios depend on the chosen origin.

Shelf length is ratio-level because zero length and ratios are meaningful.

**State the conclusion and its limits**

Renewal count is absolute.

Valid transformations are one-to-one relabeling for nominal data, increasing relabeling for ordinal data, positive affine transformation for years, unit multiplication for length, and no arbitrary rescaling of exact counts.

### T01-A02-V03: Data from a walking-route study

**Identify the issue**

Route number is nominal, not a quantity.

Surface type is nominal.

**Reason through the evidence**

Difficulty category is ordinal.

The local east-west map coordinate is interval-level: coordinate differences are meaningful, but zero is an arbitrary local origin, so ratios are not.

**State the conclusion and its limits**

Route distance is ratio-level, supporting meaningful zero and ratios.

Pedestrian count is absolute.

Thus equality applies to labels, order to difficulty, differences to coordinates, ratios to distance, and integer counting operations to pedestrians.

### T01-A02-V04: Community-theater measurements

**Identify the issue**

Costume tag and production genre are nominal.

Audience-prize ranking is ordinal.

**Reason through the evidence**

Fahrenheit temperature is interval-level because equal temperature differences are meaningful but 0°F is not absence of thermal energy.

Performance duration is ratio-level: zero minutes means no elapsed performance and ratios are interpretable.

**State the conclusion and its limits**

Scene-change count is absolute.

Replacing tag numbers by other unique labels changes no information; treating their numeric gaps as measurements would create fictitious information.

### T01-A02-V05: Variables in a coastal-monitoring file

**Identify the issue**

Sensor serial number and shoreline material are nominal.

Erosion-risk class is ordinal.

**Reason through the evidence**

Observation year is interval-level on a stated calendar.

Water depth is ratio-level when measured from the defined zero surface, and nesting-site count is absolute.

**State the conclusion and its limits**

The serial number remains nominal because subtraction, ordering, or averaging reflects assignment rules rather than sensor properties.

Transformations must preserve only category identity for serial number and material, order for risk, differences for year, ratios for depth, and exact units for the count.

### T01-A02-V06: A digital-humanities dataset

**Identify the issue**

Manuscript record code and writing-system category are nominal.

Preservation rank is ordinal.

**Reason through the evidence**

Historical year is interval-level on a common calendar, with meaningful differences but an arbitrary calendar origin.

File size is ratio-level under unit changes such as megabytes to bytes.

**State the conclusion and its limits**

Annotated-page count is absolute.

The corresponding admissible transformations are relabeling, order-preserving relabeling, positive affine calendar conversion, positive unit scaling, and identity-preserving counting, respectively.

### T01-A02-V07: Food-cooperative delivery data

**Identify the issue**

Vendor number and product category are nominal.

Freshness grade is ordinal.

**Reason through the evidence**

Celsius storage temperature is interval-level.

Shipment mass is ratio-level, and crate count is absolute.

**State the conclusion and its limits**

Ordering vendor numbers is not substantive; ordering freshness is.

Temperature differences such as 4°C are meaningful, but temperature ratios are not.

Both differences and ratios can be meaningful for mass, while crates have a fixed natural counting unit.

### T01-A02-V08: Information from a music workshop

**Identify the issue**

Participant code and instrument family are nominal.

Audition placement is ordinal because first precedes second without a fixed gap.

**Reason through the evidence**

Tuning offset in cents is interval-level around a conventional reference: differences are meaningful, but a zero offset is not absence of pitch.

Practice duration is ratio-level.

**State the conclusion and its limits**

Pieces performed is an absolute count.

Averages of codes or family labels have no interpretation, whereas arithmetic on durations and counts can answer substantive questions.

### T01-A02-V09: Municipal-service records

**Identify the issue**

Request ID and service department are nominal.

Priority level is ordinal.

**Reason through the evidence**

Calendar year is interval-level.

Response time is ratio-level, assuming zero hours represents no delay, and follow-up calls form an absolute count.

**State the conclusion and its limits**

The digits in an ID carry only equality information.

Year differences survive calendar shifts, response-time ratios survive unit conversion, and a count’s unit remains one call.

### T01-A02-V10: Ecological field observations

**Identify the issue**

Plot label and habitat class are nominal.

**Reason through the evidence**

Canopy-condition rank is ordinal.

Elevation relative to sea level is interval-level because sea level is a chosen reference and negative values are possible.

**State the conclusion and its limits**

Trunk diameter is ratio-level, and tree count is absolute.

Meaning is preserved by one-to-one relabeling for nominal variables, monotone recoding for rank, positive affine reference changes for elevation, positive unit scaling for diameter, and the natural count unit for trees.

## A03: Choosing Mean, Median, and Mode

### T01-A03-V01: Farmers-market summaries

**Identify the issue**

Vendor category supports a mode and proportions, not mean or median.

**Reason through the evidence**

Waiting time is ratio-level: report a mean and SD when its shape is reasonably balanced, but a median and IQR when long waits create right skew.

Freshness rating is ordinal, so mode, median, and category proportions respect its information.

**State the conclusion and its limits**

Stall number is an identifier and has no meaningful center beyond a mode if repeated.

Basket cost is ratio-level; mean reflects total spending per basket, while median better represents a typical basket under skew.

### T01-A03-V02: Community-radio data

**Identify the issue**

Program genre is nominal, so use the mode and proportions.

**Reason through the evidence**

Episode duration is ratio-level; mean and median are both valid, with skew determining which is more representative.

Favorite-episode ranking is ordinal and supports a median and mode, not a mean without an equal-gap convention.

**State the conclusion and its limits**

Station call sign is nominal, so its mode may be counted but it must not be averaged.

Donation amount is ratio-level but often right-skewed, making median and IQR primary while the mean remains useful for total revenue per donor.

### T01-A03-V03: Public-archive requests

**Identify the issue**

Request type is nominal and supports a mode.

**Reason through the evidence**

Processing days are ratio-level, so mean and median are valid; long cases often make the median more representative.

Urgency category is ordinal and supports median, mode, and proportions.

**State the conclusion and its limits**

Archive box code is nominal and should not receive numeric center summaries.

Pages delivered are an absolute count; a mean answers average workload, while a median may better describe a typical request if a few deliveries are very large.

### T01-A03-V04: Bicycle-share records

**Identify the issue**

Bicycle model is nominal and supports a mode.

Trip duration is ratio-level; report median under common right skew and mean when total time per trip matters.

**Reason through the evidence**

Maintenance-priority rank is ordinal, favoring median, mode, and the category distribution.

Docking-station ID is nominal.

**State the conclusion and its limits**

Rider age is ratio-level in ordinary demographic use, so mean and median are valid; the observed age distribution determines representativeness.

No center statistic alone describes group mixture or spread.

### T01-A03-V05: Adult-learning workshop data

**Identify the issue**

Workshop format is nominal, so use mode and proportions.

Attendance hours are ratio-level and support both mean and median.

**Reason through the evidence**

Confidence category is ordinal and favors median, mode, and category frequencies.

Registration number is a nominal identifier.

**State the conclusion and its limits**

A 0–100 assessment score is typically treated as interval-level, so a mean is defensible if equal score differences have comparable meaning; median remains valuable under skew or ceiling effects.

The equal-interval interpretation should be stated.

### T01-A03-V06: Neighborhood-tree inventory

**Identify the issue**

Tree species is nominal, so its mode gives the most common species.

**Reason through the evidence**

Trunk circumference is ratio-level and supports mean and median; unusual mature trees may make the median more representative.

Health class is ordinal and supports a median, mode, and proportions.

**State the conclusion and its limits**

Inventory tag is nominal.

Cavity count is absolute; both mean and median are valid, but many zeros and a few large counts often favor the median plus a frequency distribution.

### T01-A03-V07: Cultural-festival records

**Identify the issue**

Event type is nominal and supports mode and proportions.

Event length is ratio-level, allowing mean and median.

**Reason through the evidence**

Satisfaction band is ordinal, so report median, mode, and distribution.

Venue code is nominal.

**State the conclusion and its limits**

Attendance count is absolute, so a mean is valid for planning totals, but a median may better represent a typical event when headline events create strong right skew.

Validity comes from scale properties; usefulness also depends on shape and purpose.

### T01-A03-V08: Local-bus service data

**Identify the issue**

Route category is nominal and supports a mode.

Delay is a quantitative difference around schedule and can be averaged, but strong right skew makes the median and IQR more representative of ordinary service.

**Reason through the evidence**

Crowding level is ordinal, so use median, mode, and proportions.

Vehicle identifier is nominal.

**State the conclusion and its limits**

Distance is ratio-level and supports mean and median.

Report the mean delay too when total passenger-time impact is the question, while labeling its sensitivity to severe delays.

### T01-A03-V09: Oral-history catalog data

**Identify the issue**

Interview language is nominal; mode and proportions describe it.

Recording length is ratio-level and supports mean or median depending on shape.

**Reason through the evidence**

Sound-quality rank is ordinal, favoring a median, mode, and category distribution.

Catalog number is nominal.

**State the conclusion and its limits**

Indexed-theme count is absolute, so mean and median are valid, with skew guiding emphasis.

For language and catalog number, a numerical center other than the most frequent category carries no substantive meaning.

### T01-A03-V10: Community-kitchen records

**Identify the issue**

Meal category is nominal and supports a mode.

Preparation time is ratio-level, so mean and median are valid; the median resists unusually long preparations.

**Reason through the evidence**

Spice level is ordinal and supports median, mode, and proportions.

Recipe ID is nominal.

**State the conclusion and its limits**

Servings produced is absolute and may be summarized by mean and median.

A mean can be scale-valid yet unrepresentative when the distribution is skewed or multimodal, so inspect the full distribution.

## A12: Comparing Alternative Graphics of the Same Data

### T01-A12-V01: Library visits on two vertical scales

**Identify the issue**

The absolute change is $132-120=12$ hundred visits, or 1,200 visits.

**Reason through the evidence**

Relative to the first quarter, it is $12/120\times100=10\%$.

Graphic B makes a 10% rise occupy most of the plotting height because only 16 hundred visits span its axis; Graphic A places it in the full zero-based range.

**State the conclusion and its limits**

For a general report, the zero-based display gives safer magnitude comparison.

A focused trend display may use the narrow scale if endpoints, units, and the nonzero baseline are prominent.

### T01-A12-V02: On-time service percentages

**Identify the issue**

The increase is $86\%-82\%=4$ percentage points.

**Reason through the evidence**

Relative to 82%, it is $4/82\times100=4.88\%$.

Bars on an 80% baseline exaggerate their length ratio because bar length normally encodes magnitude from zero.

**State the conclusion and its limits**

Use zero-based bars for direct magnitude comparison, or use a labeled dot or line chart for small changes with the narrowed range disclosed.

Both “4 percentage points” and “4.88% relative increase” should be labeled accurately.

### T01-A12-V03: Park-use pictograms

**Identify the issue**

Relative to 240, the visit ratios are $252/240=1.05$ and $258/240=1.075$, increases of 5% and 7.5%.

**Reason through the evidence**

If both icon dimensions use these ratios, areas become $1.05^2=1.1025$ and $1.075^2=1.1556$, suggesting increases of 10.25% and 15.56%.

**State the conclusion and its limits**

The area exaggerates the values.

Equal-width, zero-based bars encode each value in one dimension and provide the defensible comparison.

### T01-A12-V04: Survey shares in flat and 3D bars

**Identify the issue**

The gap is $52\%-48\%=4$ percentage points.

**Reason through the evidence**

A baseline at 45% makes the visible bar lengths 3 and 7 units, a ratio of $7/3$, even though the shares are close.

Perspective adds an unrelated width cue.

**State the conclusion and its limits**

Redraw flat, equal-width bars from zero, or use two labeled points on a percentage axis with the narrowed range made explicit.

The caption should report the 4-point difference and sample basis.

### T01-A12-V05: Event registrations in chronological and reordered displays

**Identify the issue**

The net change is $320-310=10$ registrations, which is $10/310\times100=3.23\%$.

**Reason through the evidence**

Chronological order reveals the decline to 300 followed by recovery; sorting values removes that sequence and answers only which week ranks lowest or highest.

**State the conclusion and its limits**

Use the line chart for change over time and a sorted bar chart only for an explicitly labeled rank comparison.

Neither order changes the values, but it changes the question a viewer can answer.

### T01-A12-V06: Recycling rates under two baselines

**Identify the issue**

The change is $66\%-61\%=5$ percentage points, or $5/61\times100=8.20\%$ relative to the first rate.

**Reason through the evidence**

The 60%–67% scale makes the change easy to inspect but visually large; the 0%–100% scale communicates the share’s magnitude.

**State the conclusion and its limits**

A narrow dot or line plot is acceptable for trend detail when the axis limits and values are conspicuous.

Zero-based bars are preferable if bar length represents the percentage itself.

### T01-A12-V07: Donation values shown with circles

**Identify the issue**

The true value ratio is $50/40=1.25$, so the second fund received 25% more.

**Reason through the evidence**

If circle diameter is multiplied by 1.25, area is multiplied by $1.25^2=1.5625$, visually implying 56.25% more area.

**State the conclusion and its limits**

Bars with equal width and lengths proportional to value use one dimension and preserve the 1.25 ratio.

Proportional-area circles would require diameter scaled by $\sqrt{1.25}$, but bars remain easier to compare.

### T01-A12-V08: Water use on a reversed axis

**Identify the issue**

Use falls by $90-84=6$ units, a decrease of $6/90\times100=6.67\%$.

**Reason through the evidence**

On the conventional axis, the line slopes downward as use falls.

**State the conclusion and its limits**

Reversing the axis makes lower use appear higher and can be mistaken for an increase.

Use an upward-increasing axis, label units and values, and state that the three observations show a 6-unit decline without attributing a cause.

### T01-A12-V09: Response rates and unequal bar widths

**Identify the issue**

The gap is $73\%-71\%=2$ percentage points.

**Reason through the evidence**

The true height ratio is $73/71=1.028$.

If the second bar is twice as wide, its area ratio becomes $2(73)/71=2.056$, suggesting more than twice the visual amount.

**State the conclusion and its limits**

Equal bar widths ensure that length, not uncontrolled area, encodes response rate.

Labels should also give denominators so equal percentages from different sample sizes are not confused.

### T01-A12-V10: Time-use shares in 3D pie and horizontal bars

**Identify the issue**

The shares sum to $35+30+20+15=100\%$.

**Reason through the evidence**

A tilt enlarges foreground area and compresses background slices, so the front 20% slice can look larger than the 30% or 35% slices.

**State the conclusion and its limits**

A horizontal zero-based bar chart uses aligned lengths, supports accurate ordering and difference judgments, and can print every percentage.

The 3D view adds perspective distortion without adding data.

## A13: Diagnosing and Repairing a Misleading Graph

### T01-A13-V01: A truncated attendance chart

**Identify the issue**

The difference is $508-492=16$, and the relative difference is $16/492\times100=3.25\%$.

**Reason through the evidence**

Starting at 488 makes the visible heights 4 and 20, visually suggesting a fivefold result.

Missing period labels also prevent a valid comparison.

**State the conclusion and its limits**

Use equal-width bars from zero with dates, population, and counts, or a labeled dot plot with the narrow scale disclosed.

The caption should state both the 16-person and 3.25% differences.

### T01-A13-V02: Unequal histogram bins drawn as counts

**Identify the issue**

There are $n=100$ observations.

**Reason through the evidence**

Relative-frequency density is $h_j=n_j/(n w_j)$, giving $20/(100\cdot2)=0.100$, $35/(100\cdot5)=0.070$, and $45/(100\cdot10)=0.045$.

**State the conclusion and its limits**

With frequency as height, areas would be 40, 175, and 450 rather than representing the frequencies.

Plot the calculated densities as heights so areas become 0.20, 0.35, and 0.45, exactly the relative frequencies, and label the vertical axis “Relative-frequency density.”

### T01-A13-V03: A dual-axis community dashboard

**Identify the issue**

Separate axes permit almost any visual overlap because each range can be tuned independently.

**Reason through the evidence**

Coincident line positions therefore do not measure association and may even pair unrelated time trends.

A repair is two vertically aligned panels with a common time axis and fully labeled y-axes.

**State the conclusion and its limits**

If association is the question, show a scatterplot of paired observations and report an appropriate numerical association with its assumptions.

Neither alternative turns a small time series into causal evidence.

### T01-A13-V04: Irregular dates with equal spacing

**Identify the issue**

The gaps are about 1, 5, and 5 months, not three equal intervals.

**Reason through the evidence**

On equal-width visual segments, the February-to-July rise is $31-22=9$, whereas the January-to-February rise is only $22-20=2$.

The actual changes per month are approximately $(22-20)/1=2$, $(31-22)/5=1.8$, and $(32-31)/5=0.2$.

**State the conclusion and its limits**

Equal spacing therefore makes the five-month rise look much faster even though its monthly rate is slightly lower; it also overstates the final monthly rate.

Use a true date axis, plot all available dates, and label the measurement unit.

### T01-A13-V05: A tilted pie chart for program enrollment

**Identify the issue**

The total is $38+33+17+12=100\%$, with descending order 38%, 33%, 17%, 12%.

**Reason through the evidence**

Perspective changes projected areas by position, so visual size no longer matches share.

**State the conclusion and its limits**

Replace the chart with labeled horizontal bars from zero in descending order.

If a pie remains, make it flat, avoid exploded slices, and print values, although angle and area comparisons remain less accurate than aligned lengths.

### T01-A13-V06: Cumulative totals labeled as monthly activity

**Identify the issue**

Monthly counts are recovered by first differences: 40 in month 1, $85-40=45$, $135-85=50$, and $190-135=55$.

**Reason through the evidence**

A cumulative series cannot decrease when counts are nonnegative, so its upward line does not itself show accelerating monthly activity.

**State the conclusion and its limits**

Either plot the monthly counts and title them accordingly, or retain cumulative totals with a “Cumulative requests” title and explain the running sum.

### T01-A13-V07: Scaled icons for workshop participation

**Identify the issue**

The participation ratio is $30/25=1.20$, a 20% increase.

**Reason through the evidence**

Scaling both height and width by 1.20 multiplies icon area by $1.20^2=1.44$, visually implying 44% more.

**State the conclusion and its limits**

Use equal-width bars with lengths 25 and 30 from zero, or repeat identical unit icons with a disclosed key.

A one-dimensional encoding preserves the intended 1.20 ratio.

### T01-A13-V08: A selected time window for river levels

**Identify the issue**

The displayed rise is $2.7-2.1=0.6$ meters, or $0.6/2.1\times100=28.57\%$ relative to the first shown day.

**Reason through the evidence**

That calculation describes four selected days, not the month.

**State the conclusion and its limits**

The report needs all 30 values, missing-data information, measurement times, the selection rule, and relevant seasonal or weather context.

Plot the full chronological record on a consistent axis and describe the four-day rise as a subperiod.

### T01-A13-V09: Small multiples with incompatible scales

**Identify the issue**

A fixed vertical movement corresponds to very different numerical changes across the panels.

**Reason through the evidence**

Panel B’s four-unit range magnifies minor fluctuation relative to Panel A’s 50-unit range, so apparent slopes and variability are not comparable.

**State the conclusion and its limits**

Use identical y-axis limits and tick spacing when direct comparison is intended.

If separate limits are necessary for local detail, label them prominently and add a standardized or common-scale companion view.

### T01-A13-V10: A percentage without its denominator

**Identify the issue**

The observed-record percentage is $12/20=60\%$, but only $20/50=40\%$ of invitees have recorded participation.

**Reason through the evidence**

The confirmed participant share among all invitees is $12/50=24\%$.

**State the conclusion and its limits**

The other 30 outcomes are missing and must not be recoded as nonparticipation.

Show recorded outcomes with counts, disclose invitations and missingness beside the graph, avoid implying a complete invitation-level rate, and investigate whether response relates to participation.

# Part II: Calculator Practice

## A04: Quantifying an Extreme Value’s Effect on the Mean

### T01-A04-V01: Reading-session counts

**Set up the calculation**

Originally, $\bar{x}=60/6=10$ and the median is $(10+10)/2=10$.

**Work through the calculation**

After 12 becomes 42, $\bar{x}=(60-12+42)/6=90/6=15$, while the median remains $(10+10)/2=10$.

**Interpret and check the result**

The mean rises by 5; the median changes by 0.

The extreme magnitude enters the mean directly, whereas the middle ranks do not move.

### T01-A04-V02: Exhibit-viewing times

**Set up the calculation**

The original sum is 96, so $\bar{x}=96/6=16$; the median is $(16+16)/2=16$.

**Work through the calculation**

With 48 in place of 18, the sum is $96-18+48=126$, giving $\bar{x}=21$.

**Interpret and check the result**

The ordered middle values remain 16 and 16, so the median is 16.

The mean increases 5 minutes while the median does not change, showing greater resistance of the median.

### T01-A04-V03: Trail-section distances

**Set up the calculation**

Initially, $\bar{x}=30/6=5$ km and $\tilde{x}=(5+5)/2=5$ km.

**Work through the calculation**

After the error, the sum is $30-7+31=54$, so $\bar{x}=9$ km.

**Interpret and check the result**

The median remains 5 km.

The mean rises by 4 km because every magnitude contributes; the order of the central observations is unchanged.

### T01-A04-V04: Digitized-page totals

**Set up the calculation**

The original sum is 126, yielding $\bar{x}=126/6=21$ pages, and $\tilde{x}=(21+21)/2=21$.

**Work through the calculation**

Replacing 24 by 84 gives sum $186$ and mean $186/6=31$, while the median stays 21.

**Interpret and check the result**

The extreme entry adds 60 to the total and therefore 10 to the mean, but it does not cross the middle ranks.

### T01-A04-V05: Queue durations

**Set up the calculation**

Originally, $\bar{x}=42/6=7$ minutes and $\tilde{x}=7$.

**Work through the calculation**

The altered sum is $42-9+39=72$, so the new mean is $72/6=12$ minutes.

**Interpret and check the result**

The middle values are still 7 and 7, leaving the median at 7.

The mean rises by 5 minutes; the median’s zero change reflects its reliance on order rather than distance from the center.

### T01-A04-V06: Workshop attendance totals

**Set up the calculation**

The original mean is $144/6=24$, and the median is $(24+24)/2=24$.

**Work through the calculation**

After 26 becomes 62, $\bar{x}=(144-26+62)/6=180/6=30$.

**Interpret and check the result**

The median remains 24.

One implausible value therefore raises the mean by 6 participants but leaves the median unchanged, signaling a need to verify the source record.

### T01-A04-V07: Archive-quality scores

**Set up the calculation**

Initially, $\bar{x}=204/6=34$ and $\tilde{x}=34$.

**Work through the calculation**

The import error gives sum $204-37+85=252$, so $\bar{x}=42$; the median remains 34.

The mean rises by 8 points.

**Interpret and check the result**

An analyst should check coding, units, provenance, and plausible range before correcting or excluding 85.

Extremeness alone is not evidence that a genuine observation is invalid.

### T01-A04-V08: Completed community tasks

**Set up the calculation**

Originally, $\bar{x}=24/6=4$ tasks and $\tilde{x}=4$.

**Work through the calculation**

Replacing 6 by 30 gives sum 48, so $\bar{x}=48/6=8$, while $\tilde{x}=4$.

**Interpret and check the result**

The doubled mean reflects total tasks divided across all six cases.

The unchanged median describes the central ordered pair and better represents the cluster of five small counts.

### T01-A04-V09: Recorded interview lengths

**Set up the calculation**

The original mean is $300/6=50$ minutes, and the median is 50.

**Work through the calculation**

The revised sum is $300-54+114=360$, yielding $\bar{x}=60$ minutes; the middle pair remains 50 and 50.

**Interpret and check the result**

Thus one entry raises the mean by 10 minutes but changes the median by 0.

Most interviews remain centered near 50 minutes.

### T01-A04-V10: Seedling-survival counts

**Set up the calculation**

Initially, $\bar{x}=78/6=13$ seedlings and $\tilde{x}=13$.

**Work through the calculation**

With 57 replacing 15, the sum becomes $78-15+57=120$, so $\bar{x}=20$, while the median remains 13.

**Interpret and check the result**

The mean increases by 7 because the changed magnitude enters the numerator.

Checking the raw record determines whether 57 is an error, a unit mismatch, or a real unusual plot.

## A05: Computing and Comparing Group Medians

### T01-A05-V01: Two gallery rooms

**Set up the calculation**

North sorts to $7,8,10,11,14$, so its median is the third value, 10 minutes.

**Work through the calculation**

South sorts to $8,9,12,13,15$, giving median 12 minutes.

**Interpret and check the result**

The sample’s central South-room visit is 2 minutes longer.

This descriptive comparison does not show that the room caused longer viewing because visitors and exhibits may differ.

### T01-A05-V02: Two cataloging teams

**Set up the calculation**

Cedar sorts to $15,16,17,18,20,21$, so $\tilde{x}=(17+18)/2=17.5$ records.

**Work through the calculation**

Maple sorts to $13,14,17,18,19,22$, also giving $(17+18)/2=17.5$.

**Interpret and check the result**

Their medians match, although the remaining values and spreads differ.

Equal medians do not make the full distributions equal.

### T01-A05-V03: Two walking routes

**Set up the calculation**

Lake sorts to $27,29,31,32,35$, with median 31 minutes.

**Work through the calculation**

Hill sorts to $30,34,36,38,41$, with median 36 minutes.

**Interpret and check the result**

The observed Hill-route median is 5 minutes higher.

This summarizes central travel time in these samples, not an adjusted route effect.

### T01-A05-V04: Two public workshops

**Set up the calculation**

Clay sorts to $3,4,5,6,7,8$, so its median is $(5+6)/2=5.5$ questions.

**Work through the calculation**

Print sorts to $2,3,4,5,7,9$, giving $(4+5)/2=4.5$.

**Interpret and check the result**

Clay’s median is one question higher.

The medians alone do not reveal ranges, clustering, or whether a few sessions were unusual.

### T01-A05-V05: Two oral-history collections

**Set up the calculation**

Harbor sorts to $41,48,50,55,62$, so the median is 50 minutes.

**Work through the calculation**

Orchard sorts to $39,44,46,52,57$, so the median is 46 minutes.

**Interpret and check the result**

The central Harbor recording is 4 minutes longer in these samples.

Spread and selection still require separate assessment.

### T01-A05-V06: Two community gardens

**Set up the calculation**

East sorts to $19,22,24,26,28,31$, producing $(24+26)/2=25$.

**Work through the calculation**

West sorts to $17,21,23,25,27,29$, producing $(23+25)/2=24$.

**Interpret and check the result**

East’s sample median exceeds West’s by one harvested item.

Sampling variability and plot differences prevent a population conclusion from this descriptive gap alone.

### T01-A05-V07: Two reading circles

**Set up the calculation**

Amber sorts to $12,14,16,18,20$, with median 16 pages.

**Work through the calculation**

Indigo sorts to $13,15,17,19,21$, with median 17 pages.

**Interpret and check the result**

Indigo’s observed center is one page higher.

A measure of spread and the full ordered data help determine whether that small gap is substantively notable.

### T01-A05-V08: Two repair desks

**Set up the calculation**

Desk One sorts to $18,20,22,24,26,30$, so $\tilde{x}=(22+24)/2=23$ minutes.

**Work through the calculation**

Desk Two sorts to $17,21,23,25,27,29$, so $\tilde{x}=(23+25)/2=24$.

**Interpret and check the result**

The central case at Desk Two took one minute longer in this dataset; no causal explanation follows from that difference.

### T01-A05-V09: Two language exchanges

**Set up the calculation**

Birch sorts to $38,42,44,47,51$, giving median 44 turns.

**Work through the calculation**

Pine sorts to $36,41,45,49,53$, giving median 45.

**Interpret and check the result**

Pine is one turn higher at the center.

An IQR, range, or complete distribution would add information about consistency that the medians omit.

### T01-A05-V10: Two conservation crews

**Set up the calculation**

Ridge sorts to $9,11,12,13,14,16$, so its median is $(12+13)/2=12.5$ plots.

**Work through the calculation**

Valley sorts to $8,10,11,14,15,17$, also giving $(11+14)/2=12.5$.

**Interpret and check the result**

The crews have equal sample medians despite different ordered values, so their complete performance patterns should not be called identical.

## A06: Sequential Mean and Median Tasks

### T01-A06-V01: Weekly translation pages

**Set up the calculation, part (a)**

Sorted values are $4,5,6,7,8$, so $\tilde{x}=6$, and $\bar{x}=30/5=6$.

**Work through the calculation, part (b)**

With missing value $m$, $(4+6+7+8+m)/5=6$, so $25+m=30$ and $m=5$.

**Interpret and check the result, part (c)**

Replacing 5 by 25 gives sum 50, mean 10, and ordered median 7. The extreme value raises the mean by 4 but moves the median only 1 because it changes the ordering near the center only slightly.

### T01-A06-V02: Community-call durations

**Set up the calculation, part (a)**

Ordered data $12,12,14,15,17$ give median 14 and mean $70/5=14$ minutes.

**Work through the calculation, part (b)**

$(12+14+15+17+m)/5=14$ gives $58+m=70$, hence $m=12$.

**Interpret and check the result, part (c)**

With 42, the sum is 100, mean 20, and ordered median 15. Four calls lie between 12 and 17, so 20 is pulled beyond that cluster and is not its typical duration.

### T01-A06-V03: Field-note entries

**Set up the calculation, part (a)**

The sorted values $20,22,23,24,26$ have median 23; the mean is $115/5=23$.

**Work through the calculation, part (b)**

$(20+22+24+26+m)/5=23$ gives $92+m=115$, so $m=23$.

**Interpret and check the result, part (c)**

Replacing it with 58 gives sum 150, mean 30, and ordered median 24. The mean rises 7 entries, while the median rises 1, showing different sensitivity.

### T01-A06-V04: Neighborhood-meeting questions

**Set up the calculation, part (a)**

Sorting gives $7,8,9,10,11$, median 9, and $\bar{x}=45/5=9$.

**Work through the calculation, part (b)**

$(7+9+10+11+m)/5=9$ yields $37+m=45$, so $m=8$.

**Interpret and check the result, part (c)**

With 28, the sum is 65 and mean 13; sorted values $7,9,10,11,28$ have median 10. One extreme count changes the mean by 4 and the median by 1.

### T01-A06-V05: Archive-box processing

**Set up the calculation, part (a)**

Ordered values $30,32,33,34,36$ give median 33; $\bar{x}=165/5=33$ minutes.

**Work through the calculation, part (b)**

$(30+32+34+36+m)/5=33$ gives $132+m=165$, so $m=33$.

**Interpret and check the result, part (c)**

With 78, sum $210$, mean 42, and median 34. The median is closer to the four ordinary times, while the mean incorporates the unusually long case.

### T01-A06-V06: Rehearsal-break counts

**Set up the calculation, part (a)**

Sorting yields $2,3,4,5,6$; median and mean are both 4 because the sum is 20.

**Work through the calculation, part (b)**

$(2+4+5+6+m)/5=4$ gives $17+m=20$, hence $m=3$.

**Interpret and check the result, part (c)**

With 18, the sum is 35, mean 7, and ordered median 5. The extreme count adds 15 to the total and 3 to the mean but moves the central rank by only one unit.

### T01-A06-V07: Market-stall visitors

**Set up the calculation, part (a)**

Sorted values $40,44,45,46,50$ give median 45; the mean is $225/5=45$ hundred.

**Work through the calculation, part (b)**

$(40+44+46+50+m)/5=45$ yields $180+m=225$, so $m=45$.

**Interpret and check the result, part (c)**

Replacing it by 85 gives sum 265, mean 53, and median 46. Four periods remain at or below 50 hundred, so the median better represents their center.

### T01-A06-V08: Exhibit-label word counts

**Set up the calculation, part (a)**

Ordered values are $9,10,11,12,13$; median and mean are 11 tens because $55/5=11$.

**Work through the calculation, part (b)**

$(9+11+12+13+m)/5=11$ gives $45+m=55$, so $m=10$.

**Interpret and check the result, part (c)**

With 35, sum 80, mean 16, and median 12. The mean responds to the full 25-unit increase; the median depends on the new middle observation.

### T01-A06-V09: Habitat-survey durations

**Set up the calculation, part (a)**

Sorting gives $16,18,19,20,22$, so median 19 and mean $95/5=19$ minutes.

**Work through the calculation, part (b)**

$(16+18+20+22+m)/5=19$ gives $76+m=95$, hence $m=19$.

**Interpret and check the result, part (c)**

With 54, sum 130, mean 26, and median 20. The extreme duration raises the mean 7 minutes but the median only 1 minute.

### T01-A06-V10: Cooperative-delivery totals

**Set up the calculation, part (a)**

Ordered values $24,26,27,28,30$ yield median 27 and mean $135/5=27$.

**Work through the calculation, part (b)**

$(24+26+28+30+m)/5=27$ gives $108+m=135$, so $m=27$.

**Interpret and check the result, part (c)**

With 72, sum 180, mean 36, and median 28. Because four days fall from 24 to 30, the median better locates their center; the mean also communicates the larger total caused by the extreme day.

## A07: Pooled Medians and Value Replacement

### T01-A07-V01: Pooling two reading groups

**Set up the calculation**

The pooled order is $2,3,5,6,8,9,11,12,14,15$, so $\tilde{x}=(8+9)/2=8.5$.

**Work through the calculation**

Replacing 5 with 10 gives middle values 9 and 10, hence median 9.5.

**Interpret and check the result**

From the original data, replacing 15 with 60 leaves the middle values 8 and 9 and the median 8.5.

The first replacement crosses central ranks; increasing a value already above them does not.

### T01-A07-V02: Combining two market periods

**Set up the calculation**

The original order is $10,12,14,16,18,20,22,24,26,28$, giving $(18+20)/2=19$.

**Work through the calculation**

With 14 changed to 21, the order around the center is $...,18,20,21,22,...$, so the median is $(20+21)/2=20.5$.

**Interpret and check the result**

Replacing the original 28 by 80 leaves the fifth and sixth positions at 18 and 20, so the median remains 19.

Rank position, not the extreme distance, controls the result.

### T01-A07-V03: Merging two archive shelves

**Set up the calculation**

The pooled order $1,2,4,5,7,8,10,11,13,14$ gives median $(7+8)/2=7.5$.

**Work through the calculation**

When 4 becomes 9, the middle pair is 8 and 9, giving 8.5.

**Interpret and check the result**

Returning to the original data and changing 14 to 40 leaves the middle pair 7 and 8, so the median stays 7.5.

Only the first replacement changes which values occupy the center.

### T01-A07-V04: Pooling two walking sessions

**Set up the calculation**

Originally, the central ordered values are 40 and 42, so $\tilde{x}=41$ hundred steps.

**Work through the calculation**

Replacing 35 with 44 yields central values 42 and 44, hence median 43.

**Interpret and check the result**

In the separate replacement 52 to 100, the central pair remains 40 and 42 and the median remains 41.

The second replacement increases magnitude without changing central ranks.

### T01-A07-V05: Combining two workshop tables

**Set up the calculation**

The pooled data order gives central values 12 and 13, so $\tilde{x}=12.5$.

**Work through the calculation**

After 9 becomes 14, the central values are 13 and 14, giving median 13.5.

**Interpret and check the result**

Starting again from the original values, changing 19 to 49 leaves 12 and 13 in positions five and six, so the median stays 12.5.

A replacement affects the median only when it changes the middle ordering.

### T01-A07-V06: Pooling two survey zones

**Set up the calculation**

The original middle pair is 27 and 28, yielding $27.5$ households.

**Work through the calculation**

With 24 replaced by 29, the ordered middle pair becomes 28 and 29, so the median is 28.5.

**Interpret and check the result**

In the separate change from 34 to 74, 27 and 28 remain central and the median remains 27.5.

The far upper value’s size is irrelevant once its rank stays above the center.

### T01-A07-V07: Combining two rehearsal sets

**Set up the calculation**

The original ordered middle values are 12 and 14, so the median is 13 measures.

**Work through the calculation**

Replacing 8 by 15 changes the middle pair to 14 and 15, giving 14.5.

**Interpret and check the result**

Replacing the original maximum 22 by 70 instead leaves 12 and 14 central, so the median remains 13.

The results follow positions five and six of ten values.

### T01-A07-V08: Pooling two visitor streams

**Set up the calculation**

The original center is $(120+125)/2=122.5$ visitors.

**Work through the calculation**

Replacing 110 with 128 changes the ordered central pair to 125 and 128, so $\tilde{x}=126.5$.

**Interpret and check the result**

In a separate change, replacing 145 with 300 retains 120 and 125 at the center, leaving 122.5.

A much larger maximum therefore need not affect a median.

### T01-A07-V09: Combining two conservation teams

**Set up the calculation**

Originally, the fifth and sixth values are 21 and 23, so $\tilde{x}=22$.

**Work through the calculation**

Replacing 17 with 24 makes 23 and 24 central, giving 23.5.

**Interpret and check the result**

Returning to the original set and replacing 31 by 71 leaves 21 and 23 central and the median at 22.

The rank shift in the first change matters; the upper-tail extension in the second does not.

### T01-A07-V10: Pooling two delivery windows

**Set up the calculation**

The original central values are 60 and 62, so the median is 61 crates.

**Work through the calculation**

Replacing 55 by 64 produces middle values 62 and 64, giving median 63.

**Interpret and check the result**

Separately replacing the original 72 by 150 retains 60 and 62 in the middle, so the median stays 61.

These are the fifth and sixth ranks because $n=10$.

## A08: Mean, Mode, Sample Variance, Sample SD, and Range

### T01-A08-V01: Story-circle contributions

**Set up the calculation**

The sum is 48, so $\bar{x}=48/8=6$; the mode is 6.

**Work through the calculation**

Deviations are $(-4,-2,-2,0,0,0,2,6)$, and their squares are $(16,4,4,0,0,0,4,36)$, summing to 64.

Thus $s^2=64/7=9.14$ and $s=\sqrt{64/7}=3.02$.

**Interpret and check the result**

The range is $12-2=10$.

Contributions center at 6, with a typical sample spread of about 3.02 contributions around that mean.

### T01-A08-V02: Exhibit label lengths

**Set up the calculation**

The values sum to 72, giving $\bar{x}=72/8=9$ lines, and 9 is the mode.

**Work through the calculation**

Deviations $(-4,-2,-2,0,0,0,2,6)$ have squared sum $64$.

**Interpret and check the result**

Therefore $s^2=64/7=9.14$, $s=3.02$ lines, and range $15-5=10$ lines.

The 15-line label contributes $6^2=36$ to the squared-deviation total.

### T01-A08-V03: Community-session questions

**Set up the calculation**

The sum is 56, so $\bar{x}=7$.

**Work through the calculation**

Values 3, 7, and 11 each occur twice, making all three modes.

Squared deviations $(16,16,4,0,0,4,16,16)$ sum to 72.

**Interpret and check the result**

Hence $s^2=72/7=10.29$, $s=\sqrt{72/7}=3.21$, and range $11-3=8$.

Multiple modes mean no single value has uniquely highest frequency.

### T01-A08-V04: Cataloging times

**Set up the calculation**

The sum is 108, so $\bar{x}=13.5$ minutes; the mode is 15.

**Work through the calculation**

The squared deviations sum to the unrounded value $12.25+2.25+2.25+0.25+2.25+2.25+2.25+6.25=30$.

**Interpret and check the result**

Thus $s^2=30/7=4.2857\ldots\approx4.29$, $s=\sqrt{30/7}=2.0701\ldots\approx2.07$ minutes, and range $16-10=6$ minutes.

Rounding occurs only in the displayed final variance and SD.

### T01-A08-V05: Daily repair requests

**Set up the calculation**

The sum is 32, giving $\bar{x}=4$, and the mode is 4.

**Work through the calculation**

Squared deviations $(9,4,4,1,0,0,0,64)$ total 82.

**Interpret and check the result**

Therefore $s^2=82/7=11.71$, $s=3.42$, and range $12-1=11$.

The value 12 contributes 64 of 82 squared-deviation units and pulls the mean above six of the eight observations.

### T01-A08-V06: Audio-segment durations

**Set up the calculation**

The sum is 188, so $\bar{x}=23.5$ seconds; 24 is the mode.

**Work through the calculation**

The deviations’ squares sum to $12.25+2.25+0.25+0.25+0.25+0.25+0.25+20.25=36$.

**Interpret and check the result**

Thus $s^2=36/7=5.14$, $s=\sqrt{36/7}=2.27$ seconds, and range $28-20=8$ seconds.

The summaries indicate a cluster near 24 with modest spread.

### T01-A08-V07: Garden-plot observations

**Set up the calculation**

The total is 60, yielding $\bar{x}=7.5$; the mode is 7.

**Work through the calculation**

Squared deviations are $12.25,2.25,0.25,0.25,0.25,0.25,2.25,20.25$, totaling 38.

**Interpret and check the result**

Therefore $s^2=38/7=5.4286\ldots\approx5.43$, $s=\sqrt{38/7}=2.3299\ldots\approx2.33$, and range $12-4=8$.

Values remain unrounded until the displayed final variance and SD.

### T01-A08-V08: Workshop check-in times

**Set up the calculation**

The sum is 280, so $\bar{x}=35$ minutes; 38 is the mode.

**Work through the calculation**

Squared deviations $(25,9,1,1,1,9,9,9)$ sum to 64.

**Interpret and check the result**

Thus $s^2=64/7=9.14$, $s=3.02$ minutes, and range $38-30=8$ minutes.

The mean is below the mode because the lowest check-ins extend farther from 35 than the highest ones.

### T01-A08-V09: Indexed-theme counts

**Set up the calculation**

The sum is 96, giving $\bar{x}=12$.

**Work through the calculation**

Both 10 and 12 occur twice, so both are modes.

Squared deviations $(9,4,4,1,0,0,1,49)$ sum to 68.

**Interpret and check the result**

Hence $s^2=68/7=9.71$, $s=3.12$, and range $19-9=10$.

The mean of 12 does not reveal that 19 contributes 49 of the 68 squared-deviation units.

### T01-A08-V10: Community-delivery intervals

**Set up the calculation**

The total is 336, so $\bar{x}=42$ minutes, which is also the mode.

**Work through the calculation**

The squared deviations $(16,4,4,0,0,0,4,36)$ total 64.

**Interpret and check the result**

Consequently, $s^2=64/(8-1)=9.14$, $s=3.02$ minutes, and range $48-38=10$ minutes.

The denominator 7 marks the corrected sample variance rather than population variance.

## A09: Equal Means Do Not Imply Similar Distributions

### T01-A09-V01: Two neighborhood reading programs

**Reason before calculating**

Both sums are 30, so both means are $30/5=6$.

**Work through the calculation**

Brook’s range is $8-4=4$; its squared-deviation sum is 10, so $s=\sqrt{10/4}=1.58$.

Field’s range is 12; its squared-deviation sum is 90, so $s=\sqrt{90/4}=4.74$.

**Interpret and check the result**

Field is three times as dispersed in SD units.

The common mean locates center but omits this large consistency difference.

### T01-A09-V02: Two archive workflows

**Reason before calculating**

Each workflow sums to 100, giving mean 20.

**Work through the calculation**

Pine has range 4 and $s=\sqrt{10/4}=1.58$.

Stone has range 20 and $s=\sqrt{250/4}=7.91$.

**Interpret and check the result**

Completion is much more tightly grouped for Pine.

Reporting “both average 20 minutes” would conceal operational variability that may matter to planning.

### T01-A09-V03: Two public-speaking groups

**Reason before calculating**

Both groups sum to 50, so $\bar{x}=10$.

**Work through the calculation**

Coral’s range is $13-7=6$, with corrected sample SD $s=\sqrt{20/(5-1)}=2.24$.

**Interpret and check the result**

Slate’s range is $18-2=16$, with corrected sample SD $s=\sqrt{200/(5-1)}=7.07$.

The same center coexists with very different lower and upper observations, so the mean cannot describe consistency.

### T01-A09-V04: Two community-event schedules

**Reason before calculating**

Each set sums to 150 and has mean 30 minutes.

**Work through the calculation**

Oak’s range is 4 and $s=\sqrt{10/4}=1.58$.

**Interpret and check the result**

Reed’s range is 40 and $s=\sqrt{1000/4}=15.81$.

Oak is more homogeneous because its events remain near 30, while Reed spans from 10 to 50.

### T01-A09-V05: Two garden harvest patterns

**Reason before calculating**

Both patterns total 30, so both means equal 6.

**Work through the calculation**

Sun’s range is $10-2=8$, with $s=\sqrt{40/4}=3.16$.

Shade’s range is 12, with $s=\sqrt{144/4}=6.00$.

**Interpret and check the result**

Shade also has repeated extremes at 0 and 12 rather than even spacing.

The mean hides both the larger spread and the different shape.

### T01-A09-V06: Two museum tour routes

**Reason before calculating**

Both routes sum to 250, yielding mean 50 minutes.

**Work through the calculation**

Glass has range 4 and $s=\sqrt{10/4}=1.58$.

Wood has range 60 and $s=\sqrt{2250/4}=23.72$.

**Interpret and check the result**

Glass is tightly predictable around 50; Wood can be 30 minutes below or above it.

Equal mean duration therefore does not imply a similar visitor experience.

### T01-A09-V07: Two local-history workshops

**Reason before calculating**

Both totals are 75, so the mean is 15 attendees.

**Work through the calculation**

Ink has range 8 and $s=\sqrt{40/4}=3.16$.

**Interpret and check the result**

Paper has range 24 and $s=\sqrt{360/4}=9.49$.

The organizer would miss that Paper attendance fluctuates three times as much in SD units, affecting staffing even though average attendance matches.

### T01-A09-V08: Two coastal survey windows

**Reason before calculating**

Each window totals 370, giving mean 74 observations.

**Work through the calculation**

Dawn’s range is $78-70=8$, with corrected sample SD $s=\sqrt{40/(5-1)}=3.16$.

Dusk’s range is $98-50=48$, with corrected sample SD $s=\sqrt{1440/(5-1)}=18.97$.

**Interpret and check the result**

Dawn is far more consistent.

The shared center says nothing about this sixfold range difference.

### T01-A09-V09: Two rehearsal sequences

**Reason before calculating**

Both sequences sum to 25 and have mean change 5.

**Work through the calculation**

Bell’s range is 8 and $s=\sqrt{40/4}=3.16$.

Drum’s range is 24 and $s=\sqrt{360/4}=9.49$.

**Interpret and check the result**

Negative values are valid changes below baseline.

Drum varies three times as much in SD units despite the identical average change.

### T01-A09-V10: Two delivery routes

**Reason before calculating**

Both sets total 125, so each mean is 25 minutes.

**Work through the calculation**

Lime has range 4 and $s=\sqrt{10/4}=1.58$.

**Interpret and check the result**

Plum has range 40 and $s=\sqrt{1000/4}=15.81$.

Lime is descriptively more predictable because its times cluster near the mean; no causal reason for that difference is established.

## A10: Linear Transformations of Mean, Variance, and SD

### T01-A10-V01: Rescaling an engagement index

**Set up the calculation**

Here $a=5$, $b=2$, and $s_x=\sqrt{9}=3$.

**Work through the calculation**

Thus $\bar{y}=5+2(12)=29$, $s_y^2=2^2(9)=36$, and $s_y=|2|(3)=6$.

**Interpret and check the result**

Adding 5 shifts every value and the mean by 5; multiplying by 2 doubles all deviations and quadruples their squared average.

### T01-A10-V02: Converting a timing score

**Set up the calculation**

With $a=-3$, $b=0.5$, and $s_x=4$, $\bar{y}=-3+0.5(20)=7$.

**Work through the calculation**

The variance is $s_y^2=0.5^2(16)=4$, and $s_y=0.5(4)=2$.

**Interpret and check the result**

Multiplication by 0.5 halves each distance from the mean; the additive constant relocates the scale without affecting dispersion.

### T01-A10-V03: Reversing a quality scale

**Set up the calculation**

Here $a=40$, $b=-3$, and $s_x=5$.

**Work through the calculation**

Therefore $\bar{y}=40-3(8)=16$, $s_y^2=(-3)^2(25)=225$, and $s_y=|-3|(5)=15$.

**Interpret and check the result**

The negative slope reverses order.

Dispersion remains nonnegative because distances use absolute magnitude and squared distances use $(-3)^2$.

### T01-A10-V04: Expanding a participation score

**Set up the calculation**

The original SD is $s_x=\sqrt{4}=2$.

**Work through the calculation**

Substitution gives $\bar{y}=10+4(15)=70$, $s_y^2=4^2(4)=64$, and $s_y=4(2)=8$.

**Interpret and check the result**

Adding 10 affects only the mean.

Multiplying by 4 multiplies SD by 4 and variance by 16.

### T01-A10-V05: Recalibrating a field index

**Set up the calculation**

The original SD is $s_x=\sqrt{36}=6$.

**Work through the calculation**

With $a=-5$ and $b=1.5$, $\bar{y}=-5+1.5(30)=40$, $s_y^2=1.5^2(36)=2.25(36)=81$, and $s_y=1.5(6)=9$.

**Interpret and check the result**

The shift lowers every transformed score by 5 after scaling but does not change spread.

### T01-A10-V06: Reflecting a response scale

**Set up the calculation**

Since $s_x=\sqrt{49}=7$, $\bar{y}=2-2(6)=-10$, $s_y^2=(-2)^2(49)=196$, and $s_y=|-2|(7)=14$.

**Work through the calculation**

The factor $-2$ reverses order and doubles distances; adding 2 then shifts every transformed value equally.

**Interpret and check the result**

Neither variance nor SD is negative.

### T01-A10-V07: Compressing an archive index

**Set up the calculation**

The original SD is 8.

**Work through the calculation**

Therefore $\bar{y}=100+0.25(50)=112.5$, $s_y^2=0.25^2(64)=4$, and $s_y=0.25(8)=2$.

**Interpret and check the result**

A quarter-scale multiplier reduces each deviation to one quarter and the variance to one sixteenth.

The 100-unit shift changes only location.

### T01-A10-V08: Shifting a conservation score

**Set up the calculation**

With $s_x=10$, $a=-20$, and $b=1.2$, $\bar{y}=-20+1.2(18)=1.6$.

**Work through the calculation**

Also, $s_y^2=1.2^2(100)=144$ and $s_y=1.2(10)=12$.

**Interpret and check the result**

The $-20$ term shifts the center but leaves deviations unchanged; 1.2 enlarges SD by 20% and variance by 44%.

### T01-A10-V09: Enlarging a short rating scale

**Set up the calculation**

The original SD is $s_x=\sqrt{1.44}=1.2$.

**Work through the calculation**

Thus $\bar{y}=7+5(9)=52$, $s_y^2=5^2(1.44)=36$, and $s_y=5(1.2)=6$ new-scale units.

**Interpret and check the result**

The additive 7 does not enter either dispersion formula.

### T01-A10-V10: Reversing and shrinking a duration index

**Set up the calculation**

The original SD is $s_x=\sqrt{121}=11$.

**Work through the calculation**

Substitution gives $\bar{y}=3-0.8(42)=-30.6$, $s_y^2=(-0.8)^2(121)=0.64(121)=77.44$, and $s_y=0.8(11)=8.8$.

**Interpret and check the result**

Squaring removes the sign because variance measures squared distances; the negative sign only reverses ordering.

## A11: Z-Standardization

### T01-A11-V01: Standardizing reading counts

**Set up the calculation**

The mean is $\bar{x}=70/5=14$.

**Work through the calculation**

The squared deviations are $16,4,0,4,16$, so $s_x=\sqrt{40/4}=\sqrt{10}=3.162$.

Substitution gives $z=(-4/\sqrt{10},-2/\sqrt{10},0,2/\sqrt{10},4/\sqrt{10})$, or $(-1.265,-0.632,0.000,0.632,1.265)$.

**Interpret and check the result**

Their exact sum is 0 and squared sum is 4, verifying mean 0 and sample SD 1.

Rounding the displayed values can create a tiny departure from those exact results.

### T01-A11-V02: Standardizing catalog totals

**Set up the calculation**

The total is 135, so $\bar{x}=27$.

**Work through the calculation**

Deviations $(-3,-1,1,1,2)$ have squared sum 16, giving $s_x=\sqrt{16/4}=2$.

Hence $z=(-1.500,-0.500,0.500,0.500,1.000)$.

**Interpret and check the result**

The z-scores sum to 0 and their squares sum to 4, so $\bar{z}=0$ and $s_z=1$.

The smallest total lies 1.5 sample SDs below the mean; the largest lies 1 SD above it.

### T01-A11-V03: Standardizing workshop durations

**Set up the calculation**

The mean is $\bar{x}=60/5=12$.

**Work through the calculation**

Squared deviations are $25,0,1,1,9$, totaling 36, so $s_x=\sqrt{36/4}=3$.

**Interpret and check the result**

The standardized values are $(-5/3,0,1/3,1/3,1)$, or $(-1.667,0.000,0.333,0.333,1.000)$.

Exact z-scores sum to 0 and have squared sum $25/9+1/9+1/9+1=4$, which verifies mean 0 and sample SD 1.

### T01-A11-V04: Standardizing visitor-flow indices

**Set up the calculation**

The total is 225, giving $\bar{x}=45$.

**Work through the calculation**

Deviations $(-5,-2,-1,3,5)$ have squared sum 64, so $s_x=\sqrt{64/4}=4$.

Thus $z=(-1.250,-0.500,-0.250,0.750,1.250)$.

**Interpret and check the result**

Their exact sum is 0 and squared sum is 4, yielding $\bar{z}=0$ and $s_z=1$.

A value with $z=0$ would equal the original mean of 45; this dataset has no observed value exactly at that mean.

### T01-A11-V05: Standardizing archive-size measures

**Set up the calculation**

The mean is $\bar{x}=570/5=114$.

**Work through the calculation**

Deviations $(-8,-1,1,3,5)$ have squared sum 100, so $s_x=\sqrt{100/4}=5$.

The z-scores are $(-1.600,-0.200,0.200,0.600,1.000)$.

**Interpret and check the result**

They sum to 0, and their squares total 4, verifying mean 0 and sample SD 1.

For example, 117 has $z=(117-114)/5=0.600$, or 0.6 SD above average.

### T01-A11-V06: Standardizing field-observation totals

**Set up the calculation**

The total is 115, so $\bar{x}=23$.

**Work through the calculation**

The deviations $(-9,-2,1,3,7)$ have squared sum 144 and $s_x=\sqrt{144/4}=6$.

Therefore $z=(-1.500,-0.333,0.167,0.500,1.167)$.

**Interpret and check the result**

Using exact fractions, the z-scores sum to 0 and their squares sum to 4, giving mean 0 and sample SD 1.

Negative signs mark totals below 23; positive signs mark totals above 23.

### T01-A11-V07: Standardizing rehearsal lengths

**Set up the calculation**

The mean is $\bar{x}=300/5=60$.

**Work through the calculation**

Deviations $(-9,-5,1,5,8)$ have squared sum 196, so $s_x=\sqrt{196/4}=7$.

The z-scores are $(-1.286,-0.714,0.143,0.714,1.143)$.

**Interpret and check the result**

Their exact sum is 0 and squared sum is $196/49=4$, verifying the standardized mean and SD.

A length of 68 is $(68-60)/7=1.143$ sample SDs above the mean.

### T01-A11-V08: Standardizing community-event counts

**Set up the calculation**

The sum is 155, giving $\bar{x}=31$.

**Work through the calculation**

Squared deviations $(100,36,4,16,100)$ total 256, so $s_x=\sqrt{256/4}=8$.

Thus $z=(-1.250,-0.750,0.250,0.500,1.250)$.

**Interpret and check the result**

Their exact sum is 0 and squared sum is 4, so $\bar{z}=0$ and $s_z=1$.

Dividing a difference by an SD cancels the original measurement unit, leaving a dimensionless relative position.

### T01-A11-V09: Standardizing digitization times

**Set up the calculation**

The mean is $\bar{x}=450/5=90$ minutes.

**Work through the calculation**

Deviations $(-7,-3,1,4,5)$ have squared sum 100, giving $s_x=\sqrt{100/4}=5$ minutes.

The z-scores are $(-1.400,-0.600,0.200,0.800,1.000)$.

**Interpret and check the result**

They sum exactly to 0 and their squares total 4, verifying mean 0 and sample SD 1.

The 83-minute observation is 1.4 sample SDs below the mean.

### T01-A11-V10: Standardizing survey-volume totals

**Set up the calculation**

The total is 720, so $\bar{x}=144$.

**Work through the calculation**

Deviations $(-7,-3,-1,2,9)$ have squared sum 144, and $s_x=\sqrt{144/4}=6$.

Therefore $z=(-1.167,-0.500,-0.167,0.333,1.500)$.

**Interpret and check the result**

Exact fractional z-scores sum to 0 and have squared sum 4, yielding $\bar{z}=0$ and $s_z=1$.

The totals 146 and 153 lie above the mean and therefore have positive z-scores.

## A14: Constructing and Interpreting a Histogram and Boxplot

### T01-A14-V01: Reading-circle session lengths

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[0,5)$ | 3 | 0.30 | 5 | 0.06 |
| $[5,10)$ | 5 | 0.50 | 5 | 0.10 |
| $[10,15)$ | 1 | 0.10 | 5 | 0.02 |
| $[15,20]$ | 1 | 0.10 | 5 | 0.02 |

The median is $(6+7)/2=6.5$, and the mode is 4.

**Work through the calculation**

The lower-half median gives $Q_1=4$; the upper-half median gives $Q_3=9$.

Thus $\mathrm{IQR}=9-4=5$, with fences $4-1.5(5)=-3.5$ and $9+1.5(5)=16.5$.

**Interpret and check the result**

The Tukey whiskers end at 3 and 10; 18 is flagged.

The histogram shows most sessions below 10 and a sparse right tail; the boxplot emphasizes the middle 50% and isolates 18.

### T01-A14-V02: Archive retrieval times

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[10,15)$ | 5 | 0.50 | 5 | 0.10 |
| $[15,20)$ | 4 | 0.40 | 5 | 0.08 |
| $[20,25)$ | 0 | 0.00 | 5 | 0.00 |
| $[25,30]$ | 1 | 0.10 | 5 | 0.02 |

The mode is 13.

**Work through the calculation**

The five-number summary is minimum 11, $Q_1=13$, median $(14+15)/2=14.5$, $Q_3=17$, and maximum 27.

Thus $\mathrm{IQR}=17-13=4$.

**Interpret and check the result**

Fences are $13-1.5(4)=7$ and $17+1.5(4)=23$.

The Tukey whiskers end at 11 and 18; 27 is flagged.

The empty 20–25 bin makes the high value’s separation explicit in the histogram; the boxplot summarizes that separation compactly.

### T01-A14-V03: Community-survey completion times

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[20,25)$ | 6 | 0.60 | 5 | 0.12 |
| $[25,30)$ | 3 | 0.30 | 5 | 0.06 |
| $[30,35)$ | 0 | 0.00 | 5 | 0.00 |
| $[35,40]$ | 1 | 0.10 | 5 | 0.02 |

The median is $(23+24)/2=23.5$; the mode is 23.

**Work through the calculation**

Quartiles are $Q_1=22$ and $Q_3=26$, so $\mathrm{IQR}=4$.

The fences are 16 and 32.

**Interpret and check the result**

The Tukey whiskers end at 20 and 27; 36 is flagged above the upper fence.

Both graphs indicate a concentrated lower cluster and right asymmetry; neither proves a population distributional form.

### T01-A14-V04: Gallery-stop durations

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[5,10)$ | 6 | 0.60 | 5 | 0.12 |
| $[10,15)$ | 3 | 0.30 | 5 | 0.06 |
| $[15,20)$ | 0 | 0.00 | 5 | 0.00 |
| $[20,25]$ | 1 | 0.10 | 5 | 0.02 |

**Work through the calculation**

The median is $(8+9)/2=8.5$, and 7 is the mode.

With $Q_1=7$ and $Q_3=11$, $\mathrm{IQR}=4$, lower fence $1$, and upper fence $17$.

**Interpret and check the result**

The Tukey whiskers end at 5 and 12; the 21-minute stop is flagged.

The histogram reveals the empty interval before 21; the boxplot provides quartile spread and a direct outlier marker.

### T01-A14-V05: Daily cataloging counts

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[30,35)$ | 6 | 0.60 | 5 | 0.12 |
| $[35,40)$ | 3 | 0.30 | 5 | 0.06 |
| $[40,45)$ | 0 | 0.00 | 5 | 0.00 |
| $[45,50]$ | 1 | 0.10 | 5 | 0.02 |

The median is $(33+34)/2=33.5$, and the mode is 33.

**Work through the calculation**

The quartiles are 32 and 36, yielding $\mathrm{IQR}=4$ and fences 26 and 42.

The Tukey whiskers end at 30 and 37; 47 is flagged.

**Interpret and check the result**

The histogram shows a right-side gap and isolated upper bin.

The boxplot shows the same right asymmetry through the distant flagged point while compressing bin-level detail.

### T01-A14-V06: Neighborhood-help requests

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[0,5)$ | 3 | 0.30 | 5 | 0.06 |
| $[5,10)$ | 6 | 0.60 | 5 | 0.12 |
| $[10,15)$ | 0 | 0.00 | 5 | 0.00 |
| $[15,20]$ | 1 | 0.10 | 5 | 0.02 |

**Work through the calculation**

The median is $(5+6)/2=5.5$, and the mode is 5.

The half-sample quartiles are $Q_1=4$ and $Q_3=8$, so $\mathrm{IQR}=4$ and the fences are $-2$ and 14.

**Interpret and check the result**

The Tukey whiskers end at 2 and 9; 16 is flagged.

The histogram preserves counts within intervals; the boxplot preserves order-based center, middle spread, and the isolated upper point.

### T01-A14-V07: Audio-clip durations

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[40,45)$ | 6 | 0.60 | 5 | 0.12 |
| $[45,50)$ | 3 | 0.30 | 5 | 0.06 |
| $[50,55)$ | 0 | 0.00 | 5 | 0.00 |
| $[55,60]$ | 1 | 0.10 | 5 | 0.02 |

**Work through the calculation**

The median is $(43+44)/2=43.5$ seconds, and the mode is 43.

The quartiles are 42 and 46, so $\mathrm{IQR}=4$, with fences 36 and 52.

**Interpret and check the result**

The Tukey whiskers end at 40 and 47; the 58-second clip is flagged.

The graphs support describing an upper isolated value, not automatically deleting it; its provenance and substantive validity still require review.

### T01-A14-V08: Workshop activity totals

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[10,15)$ | 3 | 0.30 | 5 | 0.06 |
| $[15,20)$ | 6 | 0.60 | 5 | 0.12 |
| $[20,25)$ | 0 | 0.00 | 5 | 0.00 |
| $[25,30]$ | 1 | 0.10 | 5 | 0.02 |

The median is $(15+16)/2=15.5$, and 15 is the mode.

**Work through the calculation**

$Q_1=14$, $Q_3=18$, and $\mathrm{IQR}=4$, producing fences 8 and 24.

The Tukey whiskers end at 12 and 19; 29 is flagged.

**Interpret and check the result**

In this sample, most totals lie from 12 to 19 with one separated high result.

No distributional population assumption is warranted from ten observations.

### T01-A14-V09: Field-note line counts

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[60,65)$ | 6 | 0.60 | 5 | 0.12 |
| $[65,70)$ | 3 | 0.30 | 5 | 0.06 |
| $[70,75)$ | 0 | 0.00 | 5 | 0.00 |
| $[75,80]$ | 1 | 0.10 | 5 | 0.02 |

**Work through the calculation**

The median is $(63+64)/2=63.5$, and the mode is 63.

Quartiles 62 and 66 give $\mathrm{IQR}=4$, lower fence 56, and upper fence 72.

**Interpret and check the result**

The Tukey whiskers end at 60 and 67; 77 is flagged.

The histogram displays the gap before 77, while the boxplot efficiently shows center, middle spread, and the potential outlier.

### T01-A14-V10: Cooperative order sizes

**Set up the calculation**

| Bin | $n_j$ | $p_j$ | Width | $h_j$ |
|---|---:|---:|---:|---:|
| $[20,25)$ | 1 | 0.10 | 5 | 0.02 |
| $[25,30)$ | 6 | 0.60 | 5 | 0.12 |
| $[30,35)$ | 2 | 0.20 | 5 | 0.04 |
| $[35,40)$ | 0 | 0.00 | 5 | 0.00 |
| $[40,45]$ | 1 | 0.10 | 5 | 0.02 |

**Work through the calculation**

The median is $(27+28)/2=27.5$, and 27 is the mode.

$Q_1=26$, $Q_3=30$, and $\mathrm{IQR}=4$, so the fences are 20 and 36.

**Interpret and check the result**

The Tukey whiskers end at 24 and 31; 41 is flagged.

The histogram shows a dense 25–30 interval and an upper gap; the boxplot shows that 41 lies beyond the fence while retaining the middle-half summary.

## A15: Comparing Histogram Bin Widths and Origins

### T01-A15-V01: Workshop-item totals at two widths

**Set up the calculation**

Scheme A has frequencies $(2,5,4,1)$.

With width 4, densities are $(0.0417,0.1042,0.0833,0.0208)$.

**Work through the calculation**

Scheme B has frequencies $(2,3,2,2,2,1)$; width 2 gives densities $(0.0833,0.1250,0.0833,0.0833,0.0833,0.0417)$.

Both total 12.

**Interpret and check the result**

The coarse display emphasizes one broad 4–8 concentration; the fine display reveals that its 4–6 part contains more observations.

The data themselves are unchanged.

### T01-A15-V02: Retrieval times under shifted origins

**Set up the calculation**

Scheme A frequencies are $(4,5,3)$, with width-5 densities $(0.0667,0.0833,0.0500)$.

**Work through the calculation**

The shifted Scheme B frequencies are $(2,5,5)$, giving densities $(0.0333,0.0833,0.0833)$.

**Interpret and check the result**

Boundary assignments move observations among bars, changing an apparent middle peak into two equal upper bars.

Neither histogram alone proves a distinct subpopulation; report the origin and consider whether the pattern persists across defensible choices.

### T01-A15-V03: Visitor counts at coarse and fine widths

**Set up the calculation**

For Scheme A, frequencies $(5,4,3)$ and width 5 yield densities $(0.0833,0.0667,0.0500)$.

**Work through the calculation**

Scheme B frequencies are $(3,2,2,3,1,1)$.

Dividing each by $12(3)=36$ gives $(0.0833,0.0556,0.0556,0.0833,0.0278,0.0278)$.

**Interpret and check the result**

The finer bins reveal local concentrations at 29–32 and 38–41 that the coarse declining sequence obscures.

With only 12 values, these features should be described cautiously.

### T01-A15-V04: Reading times under shifted four-unit bins

**Set up the calculation**

Scheme A counts are $(3,5,4)$, so its width-4 densities are $(0.0625,0.1042,0.0833)$.

**Work through the calculation**

Scheme B counts are $(1,4,5,2)$, with densities $(0.0208,0.0833,0.1042,0.0417)$.

**Interpret and check the result**

Moving the origin by 2 units changes which observations share a bin and shifts the tallest bar from 8–12 to 10–14.

It does not change any reading time or support a different numerical center.

### T01-A15-V05: Delivery intervals at two resolutions

**Set up the calculation**

Scheme A frequencies are $(3,4,4,1)$.

**Work through the calculation**

With width 8, densities are $(0.0313,0.0417,0.0417,0.0104)$.

Scheme B places two observations in each of six bins; width 4 therefore gives density $2/[12(4)]=0.0417$ in every bin.

**Interpret and check the result**

The finer display reveals evenly spaced pairs, while the coarse bins create lower counts at the edges because their boundaries extend beyond the observed range.

Both preserve total area 1.

### T01-A15-V06: Catalog indices under shifted six-unit bins

**Set up the calculation**

Scheme A frequencies $(4,4,3,1)$ give densities $(0.0556,0.0556,0.0417,0.0139)$.

**Work through the calculation**

Scheme B frequencies $(2,4,4,2)$ give $(0.0278,0.0556,0.0556,0.0278)$, since each bin has width 6.

**Interpret and check the result**

The first origin suggests tapering at the high end; the shifted origin looks more balanced.

This sensitivity argues for examining observations and more than one substantively reasonable origin.

### T01-A15-V07: Survey counts at five- and three-unit widths

**Set up the calculation**

Scheme A has frequencies $(5,3,3,1)$; dividing by $12(5)=60$ gives densities $(0.0833,0.0500,0.0500,0.0167)$.

**Work through the calculation**

Scheme B has frequencies $(3,2,2,2,2,1)$; dividing by 36 gives $(0.0833,0.0556,0.0556,0.0556,0.0556,0.0278)$.

**Interpret and check the result**

The coarse first bar merges the repeated 20s with values through 24, making the low-end concentration look broader.

The finer view locates it more precisely.

### T01-A15-V08: Event durations with a shifted origin

**Set up the calculation**

Scheme A frequencies are $(3,4,4,1)$, producing width-6 densities $(0.0417,0.0556,0.0556,0.0139)$.

**Work through the calculation**

Scheme B frequencies are $(1,4,4,3)$, producing $(0.0139,0.0556,0.0556,0.0417)$.

**Interpret and check the result**

The apparent sparse tail switches sides when the origin moves, even though the central two bars remain equal.

Any claim of skew from one bin origin would therefore be fragile.

### T01-A15-V09: Evenly spaced scan totals

**Set up the calculation**

Each of Scheme A’s three bins contains 4 observations, so every density is $4/[12(12)]=0.0278$.

**Work through the calculation**

Each of Scheme B’s six bins contains 2 observations, so every density is $2/[12(6)]=0.0278$.

**Interpret and check the result**

Both views support even coverage across the displayed range.

Here the conclusion is stable because spacing aligns evenly at both resolutions, though a histogram still summarizes rather than reproduces exact values.

### T01-A15-V10: Clustered route durations

**Set up the calculation**

Scheme A frequencies are $(6,4,2)$; width 10 gives densities $(0.0500,0.0333,0.0167)$, suggesting a decline.

**Work through the calculation**

Scheme B has frequencies $(3,3,3,3)$; width 6 gives density $3/[12(6)]=0.0417$ in every bin.

**Interpret and check the result**

The alternate boundaries divide the four three-value clusters evenly and mask their gaps, while the coarse view merges the first two clusters.

Inspecting a dot plot alongside either histogram would expose the exact grouping.
