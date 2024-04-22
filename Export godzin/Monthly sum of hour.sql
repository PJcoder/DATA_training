SELECT date_trunc('month', dzien) AS miesiac, sum(przepracowane) as suma_godzin
     FROM czas_pracy
 GROUP BY miesiac;