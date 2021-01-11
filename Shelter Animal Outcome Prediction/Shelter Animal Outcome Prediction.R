library(dplyr)
library(data.table)
library(tidyverse)
library(data.table)
library(stringr)
library(lubridate)
library(readr)
library(GGally)
library(caret)
library(tidyr)
library(caTools)
library(MASS)
library(glmnet)

# To run this code, please change the path in this commend into the folder your "shelterdata.csv" located
# If this file and "shelterdata.csv" is under the same folder, please # this line of code
setwd("")

############################
#### Data Preprocessiog ####
############################

df<- read.csv("shelterdata.csv")
# Fullfill the missing value, have name--Named and don't have name--Unnamed
df$Name<- ifelse(df$Name=="","Unnamed","Named")
df$AgeuponOutcome<- as.character(df$AgeuponOutcome)
df$AgeuponOutcome[df$AgeuponOutcome==""]<-"NA" 

# Change the age to a uniform unite
# Select different unit year,month, week, day
df1<-df[grep("year",df$AgeuponOutcome), ]
df2<- df[grep("month",df$AgeuponOutcome),]
df3<- df[grep("week",df$AgeuponOutcome),]
df4<- df[grep("day",df$AgeuponOutcome),]
df5<- df[grep("NA",df$AgeuponOutcome),]
# Extract number and transform them to month
# Year*12
year<-gsub('([A-z]+) *','',df1$AgeuponOutcome)
year<-as.numeric(year)
df1$AgeuponOutcome<- year*12
# Keep month
Month<-gsub('([A-z]+) *','',df2$AgeuponOutcome)
Month<-as.numeric(Month)
df2$AgeuponOutcome<- Month
# Change week
Week<-gsub('([A-z]+) *','',df3$AgeuponOutcome)
Week<- as.numeric(Week)
df3$AgeuponOutcome<-round(Week/4.28,1)
# Change day
day<-gsub('([A-z]+) *','',df4$AgeuponOutcome)
day<- as.numeric(day)
df4$AgeuponOutcome<-round(day/30,2)

# Combine these subsets
cleaned_dataset<-rbind(df1,df2,df3,df4,df5)

# Change the sex outcome to sex and neuter if male=1 female=0 nm=-1 sfemale=-2
cleaned_dataset$SexuponOutcome<- as.character(cleaned_dataset$SexuponOutcome)
cleaned_dataset$SexuponOutcome[cleaned_dataset$SexuponOutcome==""]<-"NA"
cleaned_dataset$Sex<- cleaned_dataset$SexuponOutcome
# If male=1 female=0 Neutered Male=-1 Spayed Female=-2
cleaned_dataset$Sex[cleaned_dataset$Sex=='Intact Male']<-"1"
cleaned_dataset$Sex[cleaned_dataset$Sex=='Neutered Male']<-"-1"
cleaned_dataset$Sex[cleaned_dataset$Sex=='Intact Female']<-"2"
cleaned_dataset$Sex[cleaned_dataset$Sex=='Spayed Female']<-"-2"
cleaned_dataset$Sex[cleaned_dataset$Sex=='Unknown']<-"NA"
cleaned_dataset$Sex<- as.numeric(cleaned_dataset$Sex)
# Gender only have 2 values: male or female
cleaned_dataset$Gender<-abs(abs(cleaned_dataset$Sex)-2)
# Create a new column called Is_Intact: no matter it is male or female, if it is not intact, it is 0, else it is 1
cleaned_dataset$Is_Intact<- ifelse(cleaned_dataset$Sex<0,0,1)

# Delete the time from Datetime
cleaned_dataset$DateTime<- format(as.POSIXct(cleaned_dataset$DateTime,format="%m/%d/%Y %H:%M"),format = '%m/%d/%Y')

# Mark purebred and Hybred
cleaned_dataset$Breed <- as.character(cleaned_dataset$Breed)
l <- length(cleaned_dataset$Breed)
mix <- grep(".Mix",cleaned_dataset$Breed)
or <- grep("./.",cleaned_dataset$Breed)
df$Breed <- as.character(cleaned_dataset$Breed)
for (i in 1:l){
  if (!(i %in% mix) & !(i %in% or)){
    cleaned_dataset[i,"Breed"] <- "Purebred"
  }
  if ((i %in% mix) | (i %in% or)){
    cleaned_dataset[i,"Breed"] <- "Hybred"
  }
}

# Mark purecolor
cleaned_dataset$Color <- as.character(cleaned_dataset$Color)
mixColor <- grep("./.",cleaned_dataset$Color)
for (i in 1:l){
  if (!(i %in% mixColor)){
    cleaned_dataset[i,"Color"] <- "Purecolor"
  }
  if (i %in% mixColor){
    cleaned_dataset[i,"Color"] <- "Mixedcolor"
  }
}

# Rename gender column
c <- sub(0,"Female",cleaned_dataset$Gender)
d <- sub(1,"Male",c)
cleaned_dataset$Gender <- d

# Rename Is_Intact column
e <- sub(0,"Neutered",cleaned_dataset$Is_Intact)
f <- sub(1,"Unneutered",e)
cleaned_dataset$Is_Intact <- f

# Change date type predictor into year, month and day
newDate <- as.Date(cleaned_dataset$DateTime, format = "%m/%d/%Y")
cleaned_dataset$Month <- month(newDate)
cleaned_dataset$Year <- year(newDate)
cleaned_dataset$Day <- day(newDate)

# Delete useless column
cleaned_dataset <- subset(cleaned_dataset, select = -SexuponOutcome )
cleaned_dataset <- subset(cleaned_dataset, select = -Sex )
cleaned_dataset <- subset(cleaned_dataset, select = -DateTime )



##########################
#### Data Preanalysis ####
##########################

cleandf <- cleaned_dataset
cleandf$AgeuponOutcome <- as.numeric(cleandf$AgeuponOutcome)
# Summary statistics by total
summary(cleandf)

# Summary statistics group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  count() %>%   
  ungroup()

# AgeuponOutcome summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  summarize(avg.AgeuponOutcome = mean(AgeuponOutcome,na.rm=T),
            med.AgeuponOutcome = median(AgeuponOutcome,na.rm=T), 
            sd.AgeuponOutcome =sd(AgeuponOutcome,na.rm=T) ) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = OutcomeType, y = AgeuponOutcome)) +
  labs(title = "Relationship between age upon outcome and Outcome Type") +
  geom_boxplot()

# Gender summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  count(Gender) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Gender, fill = OutcomeType)) +
  labs(title = "Relationship between Gender and Outcome Type") +
  geom_bar(position = "stack")

# Name summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  count(Name) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Name, fill = OutcomeType)) +
  labs(title = "Relationship between having name or not and Outcome Type") +
  geom_bar(position = "stack")

# Is_Intact summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  count(Is_Intact) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Is_Intact, fill = OutcomeType)) +
  labs(title = "Relationship between neuter/intact and Outcome Type") +
  geom_bar(position = "stack")

# AnimalType summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  count(AnimalType) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = AnimalType, fill = OutcomeType)) +
  labs(title = "Relationship between AnimalType and Outcome Type") +
  geom_bar(position = "stack")

# Year summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  summarize(avg.Year = mean(Year,na.rm=T),
            med.Year = median(Year,na.rm=T), 
            sd.Year =sd(Year,na.rm=T) ) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Year, fill = OutcomeType)) +
  labs(title = "Relationship between Year and Outcome Type") +
  geom_bar(position = "stack")

# Month summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  summarize(avg.Month = mean(Month,na.rm=T),
            med.Month = median(Month,na.rm=T), 
            sd.Month =sd(Month,na.rm=T) ) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Month, fill = OutcomeType)) +
  labs(title = "Relationship between Month and Outcome Type") +
  geom_bar(position = "stack")

# Day summary group by OutcomeType
cleandf %>%
  group_by(OutcomeType) %>%
  summarize(avg.Day = mean(Day,na.rm=T),
            med.Day = median(Day,na.rm=T), 
            sd.Day =sd(Day,na.rm=T) ) %>%   
  ungroup()
ggplot(data = cleandf, aes(x = Day, fill = OutcomeType)) +
  labs(title = "Relationship between Day and Outcome Type") +
  geom_bar(position = "stack")

## Top 20 breeds positive/negative situation
breed <- df$Breed
mixblood <- ".Mix"
breed <- str_replace_all(breed, mixblood, " ")
breed <- str_trim(breed)
breed <- strsplit(breed,"/")
# Count breed frequency
breedChar <- unlist(breed)
data <- as.data.frame(table(breedChar))
colnames(data) <- c("Breed","Freq")
breedFreq <- data[order(data$Freq,decreasing=T),]
# Count the positive and negative case number of top 20 breeds
# Define a function to count positive case number
Pcount <- function(breedName){
  index <- grep(breedName,df$Breed)
  p <- 0
  for(i in index){
    if(df[i,"OutcomeType"] == "Positive"){
      p <- p+1
    }
  }
  return(p)
}
# Define a function to count negative case number
Ncount <- function(breedName){
  index <- grep(breedName,df$Breed)
  n <- 0
  for(i in index){
    if(df[i,"OutcomeType"] == "Negative"){
      n <- n+1
    }
  }
  return(n)
}
# Creat two lists of count results
top20 <- as.character(breedFreq[1:20,1])
positiveCount <- c()
negativeCount <- c()
for(bn in top20){
  positiveCount <- c(positiveCount,Pcount(bn))
  negativeCount <- c(negativeCount,Ncount(bn))
}
# Generate new data frame
top20df <- data_frame(Breed=top20, Positive=positiveCount, Negative=negativeCount)
top20df <- mutate(top20df, Freq = Positive + Negative, 
                  PositiveRate = Positive/Freq)
# Draw bar chart of top 20 breeds positive/negative situation
ggplot(top20df, aes(x=reorder(Breed,Freq),y=Freq,fill=PositiveRate)) +
  labs(title = "Top 20 most frequent breeds", x = "Breed") +
  geom_bar(stat = "identity") + 
  geom_text(aes(label=Freq),hjust = 0.5) +
  scale_fill_gradientn(colours=rainbow(2))+
  coord_flip()

## Top 20 colors positive/negative situation
# Clean text format
color <- df$Color
color <- str_trim(color)
color <- strsplit(color,"/")
# Count color frequency
colorChar <- unlist(color)
colorData <- as.data.frame(table(colorChar))
colnames(colorData) <- c("Color","Freq")
colorFreq = colorData[order(colorData$Freq,decreasing=T),]
# Count the positive and negative case number of top 20 colors
# Define a function to count positive case number
Pcount1 <- function(colorName){
  index <- grep(colorName,df$Color)
  p <- 0
  for(i in index){
    if(df[i,"OutcomeType"] == "Positive"){
      p <- p+1
    }
  }
  return(p)
}
# Define a function to count negative case number
Ncount1 <- function(colorName){
  index <- grep(colorName,df$Color)
  n <- 0
  for(i in index){
    if(df[i,"OutcomeType"] == "Negative"){
      n <- n+1
    }
  }
  return(n)
}
# Creat two lists of count results
top20c <- as.character(colorFreq[1:20,1])
positiveCountc <- c()
negativeCountc <- c()
for(cn in top20c){
  positiveCountc <- c(positiveCountc,Pcount1(cn))
  negativeCountc <- c(negativeCountc,Ncount1(cn))
}
# Generate new data frame
top20cdf <- data_frame(Color=top20c, Positive=positiveCountc, Negative=negativeCountc)
top20cdf <- mutate(top20cdf, Freq = Positive + Negative, 
                   PositiveRate = Positive/Freq)
# Draw bar chart of top 20 colors positive/negative situation
ggplot(top20cdf, aes(x=reorder(Color,Freq),y=Freq,fill=PositiveRate)) +
  labs(title = "Top 20 most frequent colors", x = "Color") +
  geom_bar(stat = "identity") + 
  geom_text(aes(label=Freq),hjust = 0.5) +
  scale_fill_gradientn(colours=rainbow(2))+
  coord_flip()


###########################
#### Linear Regression ####
###########################

# Data Partition
cleandf$OutcomeType <- ifelse(cleandf$OutcomeType=='Negative',0,1)
cleandf <- na.omit(cleandf)
n <- nrow(cleandf)
test_split <- sample(1:n,0.2*n,replace=FALSE)
cleandf_test <- cleandf[test_split,]
cleandf_train <- cleandf[-test_split,]
table(cleandf_train$OutcomeType)

# Linear Regression
linear_model <- train(OutcomeType~
                        Name+
                        Day+
                        Month+
                        Year+
                        AnimalType+
                        AgeuponOutcome+
                        Breed+
                        Color+
                        Gender+
                        Is_Intact,
                      data=cleandf_train,
                      method='lm',
                      trControl = trainControl(method = "repeatedcv",
                                               repeats = 3, number = 5,
                                               savePredictions = T))
summary(linear_model)
linear_model$resample

##testing misclassification
test_error <- sum(ifelse(predict(linear_model,cleandf_test)>0.5,1,0) !=cleandf_test$OutcomeType)/nrow(cleandf_test)
test_error


#############################
#### Logistic Regression ####
#############################

# Check whether the data is balanced
cleandf <- cleaned_dataset
cleandf$AgeuponOutcome <- as.numeric(cleandf$AgeuponOutcome)
table(cleandf$OutcomeType, useNA="ifany")

# Remove missing values
cleandf <- na.omit(cleandf)
table(cleandf$OutcomeType, useNA="ifany")
summary(cleandf)

# Next we partition the dataset
data_split <- createDataPartition(y=cleandf$OutcomeType,
                                  p=.75,
                                  list=F)
training <- cleandf[data_split,]
testing <- cleandf[-data_split,]

# We are predicting the probability of the non-reference level
training$OutcomeType<-factor(training$OutcomeType,levels = c("Negative","Positive"),order=TRUE)
testing$OutcomeType <- factor(testing$OutcomeType,levels = c('Negative','Positive'), order = TRUE)

# Build the logistic regression model
cleandf_glm_cv <- train(OutcomeType ~ 
                     Name +
                     Day+
                     Month+
                     Year+
                     AnimalType+
                     AgeuponOutcome+
                     Breed+
                     Color+
                     Gender+
                     Is_Intact, 
                   data = training,
                   method = "glm", family = "binomial",
                   trControl = trainControl(method = "repeatedcv",
                                            repeats = 3, number = 5,
                                            savePredictions = T))
prediction <- predict(cleandf_glm_cv, testing, type="prob")

# Call the summary to check the coefficients
summary(cleandf_glm_cv)

# Check the folds
cleandf_glm_cv$resample

# Use the model to predict the new data
class_predictions <- predict(cleandf_glm_cv, newdata = testing)

# Check the accuray of model
confusionMatrix(data = class_predictions, reference = testing$OutcomeType,
                positive = "Positive")

# Build a new model with some unimportamt features dropped
cleandf_glm_cv2 <- train(OutcomeType ~ 
                      #Day
                      Name+
                      #Month+
                      Year+
                      AnimalType+
                      AgeuponOutcome+
                      #Breed+
                      #Color+
                      Gender+
                      Is_Intact, 
                    data = cleandf,
                    method = "glm", family = "binomial",
                    trControl = trainControl(method = "repeatedcv",
                                             repeats = 3, number = 5,
                                             savePredictions = T))
prediction <- predict(cleandf_glm_cv2, testing, type="prob")

# Call the summary to check the coefficients
summary(cleandf_glm_cv2)

# Check the folds
cleandf_glm_cv2$resample

# Use the new model to predict the new data
class_predictions2 <- predict(cleandf_glm_cv2, newdata = testing)

# Check the accuray of the new model
confusionMatrix(data = class_predictions2, reference = testing$OutcomeType,
                positive = "Positive")

# LASSO logistics regression
training_x <-model.matrix(~.,training[,c('Name','AnimalType','AgeuponOutcome','Breed','Color','Gender',
                                         'Is_Intact','Month','Year','OutcomeType')])[,-1]
training_y <- training_x[,9]
training_x <- training_x[,-9]

cv.lasso <-cv.glmnet(training_x, training_y, alpha = 1, family = "binomial")

lasso_model <- glmnet(training_x, training_y, alpha = 1, family = "binomial",
                      lambda = cv.lasso$lambda.min)

testing_x <-model.matrix(~.,testing[,c('Name','AnimalType','AgeuponOutcome','Breed','Color','Gender',
                                       'Is_Intact','Month','Year','OutcomeType')])[,-1]

testing_y <-testing_x[,9]
testing_x <-testing_x[,-9]
mean(ifelse(predict(lasso_model,testing_x)>.5,'Positive','Negative') != testing$OutcomeType)

cleandf_glmnet <- train(OutcomeType ~ 
                          Day+
                          Name+
                          Month+
                          Year+
                          AnimalType+
                          AgeuponOutcome+
                          Breed+
                          Color+
                          Gender+
                          Is_Intact, 
                        data = training,
                        method = "glmnet", family = "binomial",
                        trControl = trainControl(method = "repeatedcv",
                                                 repeats = 3, number = 5,
                                                 savePredictions = T))
Regular_predictions <- predict(cleandf_glmnet, newdata = testing)

#check the accuray of model
confusionMatrix(data = Regular_predictions, reference = testing$OutcomeType,
                positive = "Positive")