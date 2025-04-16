data <- read.table("clipboard", header = FALSE, sep = "", fill = TRUE, dec = ",", stringsAsFactors = FALSE)

library(dplyr)
library(lubridate)


data <- data %>%
  mutate(
    datum = ymd(V1),
    pocet_navstev = as.integer(V2),
    trzba = as.integer(gsub("[^0-9]", "", iconv(V3, "UTF-8", "ASCII", sub = "")))
  ) %>%
  select(datum, pocet_navstev, trzba)

str(data)
head(data)

data <- data %>%
  mutate(pocet_navstev = ifelse(pocet_navstev <= 1, NA, pocet_navstev))
data <- data %>%
  mutate(trzba = ifelse(trzba <= 1, NA, trzba))

library(ggplot2)

# Graf pro hodnotu 1
ggplot(data, aes(x = datum, y = pocet_navstev)) +
  geom_line(color = "steelblue", linewidth = 1) +
  labs(title = "Časová řada - hodnota 1", x = "Datum", y = "počet návštěv") +
  theme_minimal()

# Graf pro hodnotu 2
ggplot(data, aes(x = datum, y = trzba)) +
  geom_line(color = "darkorange", linewidth = 1) +
  labs(title = "Časová řada - hodnota 2", x = "Datum", y = "trzba") +
  theme_minimal()


