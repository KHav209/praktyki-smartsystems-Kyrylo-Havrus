
PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS zamowienia;
DROP TABLE IF EXISTS produkty;
DROP TABLE IF EXISTS klienci;

CREATE TABLE klienci (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    imie TEXT NOT NULL,
    nazwisko TEXT NOT NULL,
    telefon TEXT,
    email TEXT
);

CREATE TABLE produkty (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa TEXT NOT NULL,
    zapach TEXT,
    pojemnosc_ml INTEGER,
    cena REAL,
    stan_magazynowy INTEGER
);

CREATE TABLE zamowienia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_klienta INTEGER NOT NULL,
    id_produktu INTEGER NOT NULL,
    ilosc INTEGER NOT NULL,
    status TEXT NOT NULL,
    data_zamowienia TEXT,
    FOREIGN KEY (id_klienta) REFERENCES klienci(id),
    FOREIGN KEY (id_produktu) REFERENCES produkty(id)
);

INSERT INTO klienci (imie, nazwisko, telefon, email) VALUES
('Kamil', 'Nowak', '500100200', 'kamil@gmail.com'),
('Adam', 'Kowalski', '500200300', 'adam@gmail.com'),
('Marek', 'Wisniewski', '500300400', 'marek@gmail.com'),
('Piotr', 'Wojcik', '500400500', 'piotr@gmail.com'),
('Tomasz', 'Kaminski', '500500600', 'tomasz@gmail.com');

INSERT INTO produkty (nazwa, zapach, pojemnosc_ml, cena, stan_magazynowy) VALUES
('Swieca cytrynowa', 'Cytryna', 200, 25.00, 10),
('Swieca waniliowa', 'Wanilia', 250, 30.00, 3),
('Swieca lawendowa', 'Lawenda', 200, 28.00, 15),
('Swieca rozana', 'Roza', 300, 35.00, 4),
('Swieca kokosowa', 'Kokos', 250, 32.00, 8),
('Swieca jablkowa', 'Jablko', 200, 24.00, 2);

INSERT INTO zamowienia (id_klienta, id_produktu, ilosc, status, data_zamowienia) VALUES
(1, 1, 2, 'wyslane', date('now', '-1 day')),
(2, 2, 1, 'nowe', date('now', '-2 days')),
(3, 3, 3, 'wyslane', date('now', '-3 days')),
(4, 4, 1, 'w przygotowaniu', date('now', '-4 days')),
(5, 5, 2, 'wyslane', date('now', '-5 days')),
(1, 2, 2, 'nowe', date('now', '-6 days')),
(2, 3, 1, 'wyslane', date('now', '-8 days')),
(3, 1, 4, 'w przygotowaniu', date('now', '-9 days')),
(4, 6, 2, 'nowe', date('now', '-2 days')),
(5, 1, 1, 'wyslane', date('now', '-1 day'));

SELECT *
FROM zamowienia
WHERE status = 'wyslane';

SELECT
    klienci.imie,
    klienci.nazwisko,
    produkty.nazwa AS produkt,
    zamowienia.ilosc,
    zamowienia.status
FROM zamowienia
JOIN klienci ON zamowienia.id_klienta = klienci.id
JOIN produkty ON zamowienia.id_produktu = produkty.id;

SELECT
    klienci.imie,
    klienci.nazwisko,
    SUM(zamowienia.ilosc * produkty.cena) AS wartosc_zamowien
FROM zamowienia
JOIN klienci ON zamowienia.id_klienta = klienci.id
JOIN produkty ON zamowienia.id_produktu = produkty.id
GROUP BY klienci.id;

SELECT
    produkty.nazwa,
    SUM(zamowienia.ilosc) AS liczba_sztuk
FROM zamowienia
JOIN produkty ON zamowienia.id_produktu = produkty.id
GROUP BY produkty.id
ORDER BY liczba_sztuk DESC
LIMIT 1;

SELECT *
FROM produkty
WHERE stan_magazynowy < 5;

SELECT *
FROM zamowienia
WHERE data_zamowienia >= date('now', '-7 days');
