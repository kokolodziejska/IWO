# **Słownik pojęć**

## **Dane i ich struktura**
- **Zbiór danych** – zestaw uporządkowanych informacji publicznych, posiadający metadane oraz określone dystrybucje dostępne w systemie.
- **Metadane** – zbiór informacji opisujących zbiór danych, obejmujący m.in. nazwę, opis, datę aktualizacji, format oraz warunki dostępu.
- **Dystrybucja** – konkretna instancja zbioru danych, dostępna w określonym formacie i udostępniana zgodnie z regułami systemu.
- **Schemat danych** – struktura opisująca pola, formaty i relacje między danymi w zbiorze, wykorzystywana do walidacji poprawności.
- **Wersja zbioru danych** – unikalna instancja zbioru danych odpowiadająca określonemu stanowi na dany moment, przechowywana w ramach wersjonowania.
- **Standard DCAT** – międzynarodowy standard opisu metadanych, zapewniający interoperacyjność katalogów danych publicznych.
- **Standard DCAT/AP** – profil aplikacyjny DCAT dla Unii Europejskiej, zapewniający zgodność opisu metadanych z wymogami instytucji UE.
- **Standard RDF** – model publikacji danych na najwyższym poziomie otwartości (5-star), umożliwiający ich powiązywanie i automatyczne przetwarzanie.
- **Walidacja danych** – proces automatycznej weryfikacji poprawności zbioru danych względem określonego schematu i standardów jakości.

## **Zarządzanie danymi**
- **Rejestr zbiorów danych** – centralna baza informacji o zbiorach danych dostępnych w systemie, zawierająca ich metadane i historię zmian.
- **Źródło danych** – podmiot lub system dostarczający dane do systemu IWO.
- **Indeks danych** – struktura umożliwiająca szybkie wyszukiwanie i dostęp do informacji w zbiorach danych.
- **Interoperacyjność danych** – zdolność do wymiany i współdziałania zbiorów danych z innymi systemami informatycznymi.
- **Harmonizacja danych** – proces ujednolicania struktury i formatów danych pochodzących z różnych źródeł.

## **Użytkownicy i role systemowe**
- **Użytkownik** – każda osoba posiadająca konto w systemie, korzystająca z dostępnych funkcji zgodnie z przypisanymi uprawnieniami.
- **Administrator** – użytkownik z najwyższym poziomem uprawnień, odpowiedzialny za konfigurację systemu, zarządzanie użytkownikami oraz moderowanie zbiorów danych.
- **Właściciel zbioru danych** – użytkownik odpowiedzialny za dany zbiór danych, posiadający prawo do jego modyfikacji, zarządzania wersjami oraz ustawień dostępu.
- **Redaktor** – użytkownik posiadający uprawnienia do edytowania treści metadanych oraz zarządzania publikacją danych.
- **Użytkownik zewnętrzny** – osoba lub system korzystający z publicznych funkcji systemu bez posiadania konta.
- **Anonimowy użytkownik** – osoba przeglądająca dane publiczne bez konieczności logowania, bez możliwości edycji czy zapisu ustawień.
- **Subskrybent** – użytkownik, który zapisał się do powiadomień o zmianach w wybranym zbiorze danych.

## **Dostęp i bezpieczeństwo**
- **Poziom uprawnień** – zakres dostępu użytkownika do funkcji systemu, definiowany przez przypisaną mu rolę.
- **Model uprawnień** – system kontroli dostępu określający, które operacje są dostępne dla poszczególnych ról użytkowników.
- **Kopia zapasowa** – archiwalna wersja zbiorów danych oraz ustawień systemowych, przechowywana na wypadek awarii lub konieczności przywrócenia danych.
- **Dwuskładnikowa autoryzacja (2FA)** – dodatkowa metoda weryfikacji tożsamości użytkownika podczas logowania w celu zwiększenia bezpieczeństwa.
- **Zgodność z RODO** – dostosowanie systemu do wymagań Rozporządzenia o Ochronie Danych Osobowych, zapewniające prawidłowe przetwarzanie danych użytkowników.

## **Przetwarzanie i prezentacja danych**
- **Widok danych** – sposób prezentacji zbioru danych w systemie, np. tabela, wykres, mapa.
- **Wizualizacja danych** – graficzne przedstawienie informacji w celu ich łatwiejszej interpretacji i analizy.
- **Filtrowanie danych** – mechanizm selekcji rekordów zbioru danych na podstawie określonych kryteriów.
- **Eksport danych** – generowanie plików z danymi w formatach dostępnych do pobrania przez użytkownika.
- **Import danych** – wczytywanie danych do systemu z plików lub źródeł zewnętrznych.
- **Transformacja danych** – konwersja struktury i formatu danych do standardu obsługiwanego przez system.
- **Raport systemowy** – wygenerowany zestaw informacji statystycznych o danych lub działaniach w systemie.

## **Subskrypcja i powiadomienia**
- **Subskrypcja zbioru danych** – mechanizm umożliwiający użytkownikowi otrzymywanie powiadomień o zmianach w wybranych zbiorach danych.
- **Powiadomienie systemowe** – komunikat informujący użytkownika o zdarzeniach, takich jak aktualizacja zbioru czy zmiana uprawnień.
- **Kanał powiadomień** – metoda przekazywania powiadomień, np. e-mail, SMS, API.

## **Integracja z systemami zewnętrznymi**
- **CKAN** – otwarta platforma do zarządzania danymi publicznymi, z którą system IWO może wymieniać informacje.
- **Integracja systemowa** – proces połączenia systemu z innymi platformami w celu wymiany danych i synchronizacji.
- **Format danych** – standard zapisu danych używany do importu i eksportu, np. CSV, JSON, XML, RDF.
- **API systemowe** – zestaw funkcji umożliwiających programistyczny dostęp do danych i operacji w systemie.

## **Monitorowanie i analiza**
- **Statystyki systemowe** – wskaźniki dotyczące funkcjonowania systemu, np. liczba pobrań zbiorów danych, aktywność użytkowników.
- **Monitorowanie API** – analiza zapytań kierowanych do interfejsu API w celu optymalizacji wydajności i bezpieczeństwa.
- **Rejestrowanie zdarzeń** – mechanizm zapisu operacji wykonywanych przez użytkowników oraz automatyczne procesy systemowe.
- **Śledzenie wersji danych** – funkcjonalność pozwalająca na odtworzenie wcześniejszych wersji zbiorów danych oraz historii zmian.
