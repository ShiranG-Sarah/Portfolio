# load
library(Hmisc)
library(tidyverse)
library(caret)
library(car)

# preprocess
raw_norm <- read.csv("C:/Users/Shiran Guo/OneDrive/Documents/Study/Design Lab/Kickstarter/official_data_file.csv")
colnames(raw_norm)
train <- raw_norm[,c("amt.pledged","goal","num.backers","arousal.score",
                     "total_len","type_score","num_backer_ratio_200",
                     "type_ratio_200","type_arousal" )]
amount.over.goal <- train$amt.pledged/train$goal
train$ratio <- ratio
str(train)

# Model 1
rg_r.1 <- lm(amount.over.goal~goal+num.backers+arousal.score+total_len+type_score+
               num_backer_ratio_200+type_ratio_200+type_arousal,
             data=train)
summary(rg_r.1)
vif(rg_r.1)

# Robutness Chect
## Remove Goal
rg_r.1g <- lm(amount.over.goal~num.backers+arousal.score+total_len+type_score+
               num_backer_ratio_200+type_ratio_200+type_arousal,
             data=train)
summary(rg_r.1g)

###############################################################################
# Model 2
rg_r.2 <- lm(ratio~goal+num.backers+arousal.score+total_len+type_score+
               num_backer_ratio_200+type_ratio_200+type_arousal,
             data=train)
summary(rg_r.2)
vif(rg_r.2)

# Robutness Chect
## Remove Goal
rg_r.2g <- lm(ratio~num.backers+arousal.score+total_len+type_score+
               num_backer_ratio_200+type_ratio_200+type_arousal,
             data=train)
summary(rg_r.2g)

## Remove Number of Backers
rg_r.2n <- lm(ratio~goal+arousal.score+total_len+type_score+
               num_backer_ratio_200+type_ratio_200+type_arousal,
             data=train)
summary(rg_r.2n)