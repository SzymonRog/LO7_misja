CREATE TABLE eu_grants(
   grant_id              INTEGER  NOT NULL PRIMARY KEY,
   project_name          TEXT     NOT NULL,
   grant_amount          FLOAT    NOT NULL,
   currency              TEXT     NOT NULL,
   implementation_months INTEGER  NOT NULL,
   signing_date          TEXT     NOT NULL,
   completion_date       TEXT     NOT NULL,
   project_status        TEXT     NOT NULL,
   description           TEXT     NOT NULL
);
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (1,'Modernizacja infrastruktury transportowej Lublin-Warszawa',285000.00,'PLN',24,'2025-11-15','2027-11-15','active','Projekt modernizacji drog krajowych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (2,'Cyfryzacja urzedow administracji publicznej',420000.00,'PLN',30,'2025-11-20','2027-05-20','active','Wdrozenie systemow e-administracji');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (3,'Zielona energia dla gmin wiejskich',195000.00,'PLN',36,'2025-11-25','2027-11-25','active','Instalacja paneli slonecznych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (4,'Program rewitalizacji srodmiescia Krakowa',550000.00,'PLN',28,'2025-12-01','2026-04-01','active','Odnowa zabytkow miejskich');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (5,'Wsparcie MSP w transformacji cyfrowej',310000.00,'PLN',24,'2025-12-05','2026-12-05','active','Szkolenia i dotacje dla firm');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (6,'Rozwoj turystyki kulturowej w Malopolsce',175000.00,'PLN',30,'2025-12-08','2027-06-08','active','Promocja dziedzictwa kulturowego');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (7,'Inteligentne systemy monitoringu srodowiska',225000.00,'PLN',18,'2025-05-10','2025-11-10','completed','Monitoring jakosci powietrza');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (8,'Budowa centrum innowacji technologicznych',680000.00,'PLN',48,'2025-08-15','2027-08-15','active','Centrum badawczo-rozwojowe');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (9,'Program edukacji cyfrowej dla seniorow',95000.00,'PLN',12,'2025-09-20','2025-09-20','active','Warsztaty komputerowe');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (10,'Modernizacja sieci wodociagowej',450000.00,'PLN',36,'2025-01-01','2026-11-01','active','Wymiana infrastruktury wodnej');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (11,'Rozbudowa infrastruktury kolejowej Gdansk-Gdynia',380000.00,'PLN',28,'2025-11-18','2027-03-18','active','Modernizacja torow i peronow');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (12,'Smart City inteligentne oswietlenie Poznan',215000.00,'PLN',20,'2025-11-22','2026-07-22','active','LED i systemy zarzadzania');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (13,'Program ochrony bioroznorodnosci Bieszczady',165000.00,'PLN',36,'2025-11-28','2027-11-28','active','Ochrona gatunkow zagrozonych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (14,'Digitalizacja archiwow panstwowych',290000.00,'PLN',30,'2025-12-03','2027-06-03','active','Skanowanie dokumentow historycznych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (15,'Wsparcie start-upow technologicznych',340000.00,'PLN',24,'2025-12-07','2026-12-07','active','Akcelerator dla mlodych firm');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (16,'Rewitalizacja zabytkowych kamienic Wroclaw',490000.00,'PLN',32,'2025-12-10','2027-08-10','active','Renowacja starowki');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (17,'Program walki ze smogiem Slask',520000.00,'PLN',36,'2025-06-15','2027-06-15','active','Wymiana piecow weglowych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (18,'Centrum badan nad AI',750000.00,'PLN',48,'2025-03-20','2027-03-20','active','Laboratorium sztucznej inteligencji');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (19,'Wsparcie rolnictwa ekologicznego',140000.00,'PLN',24,'2025-08-10','2026-08-10','active','Dotacje dla ekofarm');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (20,'Modernizacja systemu kanalizacyjnego',85000.00,'PLN',18,'2025-10-05','2026-04-05','active','Naprawa sieci kanalizacyjnej');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (21,'Program rozwoju e-zdrowia',410000.00,'PLN',30,'2025-11-17','2027-05-17','active','Platformy telemedyczne');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (22,'Budowa sciezek rowerowych Mazowsze',195000.00,'PLN',24,'2025-11-23','2026-11-23','active','Infrastruktura dla rowerzystow');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (23,'Wsparcie organizacji pozarzadowych',125000.00,'PLN',18,'2025-12-02','2026-06-02','active','Granty dla NGO');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (24,'Modernizacja bibliotek publicznych',235000.00,'PLN',28,'2025-12-06','2027-04-06','active','Cyfryzacja zbiorow');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (25,'Program przeciwdzialania wykluczeniu cyfrowemu',280000.00,'PLN',30,'2025-12-09','2027-06-09','active','Dostep do internetu dla wykluczonych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (26,'Rozwoj infrastruktury sportowej',620000.00,'PLN',40,'2025-09-12','2027-01-12','active','Budowa hal sportowych');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (27,'Program bezpieczenstwa zywnosciowego',95000.00,'PLN',15,'2025-07-20','2025-10-20','active','Kontrola jakosci zywnosci');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (28,'Wsparcie przedsiebiorczosci kobiet',155000.00,'PLN',24,'2025-10-15','2026-10-15','active','Szkolenia i doradztwo');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (29,'Modernizacja systemu ratownictwa medycznego',540000.00,'PLN',36,'2025-05-08','2026-05-08','active','Nowe ambulanse i sprzet');
INSERT INTO eu_grants(grant_id,project_name,grant_amount,currency,implementation_months,signing_date,completion_date,project_status,description) VALUES (30,'Program ochrony dziedzictwa kulturowego',72000.00,'PLN',12,'2025-09-25','2025-09-25','active','Konserwacja zabytkow');


CREATE TABLE contractors(
   contractor_id   INTEGER NOT NULL PRIMARY KEY,
   company_name    TEXT    NOT NULL,
   nip             INTEGER NOT NULL,
   regon           INTEGER NOT NULL,
   country         TEXT    NOT NULL,
   city            TEXT    NOT NULL,
   founded_year    INTEGER NOT NULL,
   employee_count  INTEGER NOT NULL,
   is_certified    INTEGER NOT NULL
);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (1,'BudoMax Sp. z o.o.',5252654789,368742156,'Poland','Warszawa',2015,145,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (2,'TechVision Solutions',7418529630,147852369,'Poland','Krakow',2018,89,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (3,'EcoEnergy Polska',9638527410,258963147,'Poland','Wroclaw',2012,67,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (4,'Renovatio Architekci',8529631470,369258147,'Poland','Poznan',2010,34,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (5,'DigiTransform Consulting',7539514826,852741963,'Poland','Gdansk',2019,56,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (6,'Heritage Tourism Group',6419528537,741963852,'Poland','Krakow',2016,28,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (7,'SmartCity Technologies',5283749615,963852741,'Poland','Lodz',2020,112,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (8,'Innovation Hub Poland',4172639485,852369741,'Poland','Warszawa',2017,203,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (9,'Silver Education Foundation',9517538426,741852963,'Poland','Lublin',2014,15,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (10,'AquaTech Infrastructure',8426391758,369147852,'Poland','Katowice',2011,178,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (11,'RailTech Modernization',7539628410,456789123,'Poland','Gdansk',2016,92,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (12,'LightSmart Systems',6428517390,789456123,'Poland','Poznan',2019,45,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (13,'BioDiversity Protection',8517396240,123789456,'Poland','Rzeszow',2013,23,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (14,'DigitalArchive Pro',9628417350,654987321,'Poland','Warszawa',2018,67,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (15,'StartupAccelerator Polska',5417382960,987321654,'Poland','Krakow',2020,34,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (16,'Heritage Renovation Group',7396284150,321654987,'Poland','Wroclaw',2009,156,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (17,'CleanAir Solutions',8249517630,147258369,'Poland','Katowice',2017,189,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (18,'AI Research Center',9517384620,963852147,'Poland','Warszawa',2015,267,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (19,'OrganicFarm Support',6384927150,852147963,'Poland','Bialystok',2011,19,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (20,'WaterWorks Engineering',7495168230,741369852,'Poland','Gdansk',2014,134,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (21,'MediTech Solutions',8362749510,369852741,'Poland','Warszawa',2016,78,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (22,'CyclePath Builders',5729384160,258741369,'Poland','Radom',2018,41,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (23,'NGO Support Foundation',9384726150,147963258,'Poland','Lublin',2012,12,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (24,'Library Modernization Corp',6249517380,852369147,'Poland','Poznan',2015,56,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (25,'Digital Inclusion Network',7518396240,963147852,'Poland','Lodz',2019,89,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (26,'SportFacility Developers',8395172640,741258963,'Poland','Krakow',2010,201,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (27,'FoodSafety Inspections',5172849360,369147258,'Poland','Szczecin',2013,28,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (28,'WomenBusiness Academy',9273648150,852963741,'Poland','Wroclaw',2017,34,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (29,'EmergencyMed Systems',6849271530,147852369,'Poland','Katowice',2011,145,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (30,'CulturalHeritage Conserv',7396248150,963258741,'Poland','Torun',2008,67,0);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (31,'CorpTech Industries',8529637410,147258963,'Poland','Warszawa',2008,523,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (32,'CorpTech Consulting',7418529630,258369147,'Poland','Warszawa',2010,412,1);
INSERT INTO contractors(contractor_id,company_name,nip,regon,country,city,founded_year,employee_count,is_certified) VALUES (33,'CorpTech Solutions',9517382640,369147258,'Poland','Warszawa',2012,389,1);


CREATE TABLE eu_founding_sources(
   source_id            INTEGER  NOT NULL PRIMARY KEY,
   fund_name            TEXT     NOT NULL,
   fund_type            TEXT     NOT NULL,
   managing_authority   TEXT     NOT NULL,
   total_budget         FLOAT    NOT NULL,
   available_budget     FLOAT    NOT NULL,
   priority_area        TEXT     NOT NULL,
   eligibility_criteria TEXT     NOT NULL
);


INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (1,'Europejski Fundusz Rozwoju Regionalnego','EU Structural Fund','Ministerstwo Funduszy i Polityki Regionalnej',15000000000.00,4500000000.00,'Infrastruktura i transport','Projekty powyzej 100k PLN');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (2,'Program Polska Cyfrowa','EU Digital Fund','Ministerstwo Cyfryzacji',8000000000.00,2100000000.00,'Cyfryzacja i e-administracja','Jednostki publiczne i MSP');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (3,'Narodowy Fundusz Ochrony Srodowiska','EU Environmental Fund','NFOSiGW',6500000000.00,1800000000.00,'Energia odnawialna','Projekty proekologiczne');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (4,'Fundusze Europejskie dla Polski Wschodniej','EU Regional Development','PARP',4200000000.00,950000000.00,'Rewitalizacja i rozwoj','Regiony Polski Wschodniej');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (5,'Program Inteligentny Rozwoj','EU Innovation Fund','Ministerstwo Rozwoju',12000000000.00,3200000000.00,'Innowacje i B+R','Przedsiebiorstwa i jednostki naukowe');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (6,'Europejski Fundusz Spoleczny Plus','EU Social Fund','Ministerstwo Rodziny i Polityki Spolecznej',7500000000.00,2400000000.00,'Edukacja i wlaczenie spoleczne','Organizacje non-profit');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (7,'Program Infrastruktura i Srodowisko','EU Infrastructure Fund','Ministerstwo Klimatu i Srodowiska',9200000000.00,2800000000.00,'Infrastruktura ekologiczna','Duze projekty infrastrukturalne');
INSERT INTO eu_founding_sources(source_id,fund_name,fund_type,managing_authority,total_budget,available_budget,priority_area,eligibility_criteria) VALUES (8,'Fundusze dla Miast','EU Urban Development','Ministerstwo Rozwoju i Technologii',5600000000.00,1400000000.00,'Rozwoj miejski','Projekty miejskie powyzej 50k mieszkancow');


CREATE TABLE grant_assignments(
   assignment_id          INTEGER  NOT NULL PRIMARY KEY,
   grant_id               INTEGER  NOT NULL,
   contractor_id          INTEGER  NOT NULL,
   source_id              INTEGER  NOT NULL,
   implementation_country TEXT     NOT NULL,
   regional_authority     TEXT     NOT NULL
);


INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (1,1,1,1,'Poland','Wojewodztwo Lubelskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (2,2,31,2,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (3,3,3,3,'Poland','Wojewodztwo Dolnoslaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (4,4,4,1,'Poland','Wojewodztwo Malopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (5,5,32,5,'Poland','Wojewodztwo Pomorskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (6,6,6,1,'Poland','Wojewodztwo Malopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (7,7,7,3,'Poland','Wojewodztwo Lodzkie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (8,8,8,5,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (9,9,9,6,'Poland','Wojewodztwo Lubelskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (10,10,10,3,'Poland','Wojewodztwo Slaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (11,11,11,1,'Poland','Wojewodztwo Pomorskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (12,12,12,8,'Poland','Wojewodztwo Wielkopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (13,13,13,3,'Poland','Wojewodztwo Podkarpackie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (14,14,33,2,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (15,15,15,5,'Poland','Wojewodztwo Malopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (16,16,16,4,'Poland','Wojewodztwo Dolnoslaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (17,17,17,3,'Poland','Wojewodztwo Slaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (18,18,18,5,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (19,19,19,3,'Poland','Wojewodztwo Podlaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (20,20,20,7,'Poland','Wojewodztwo Pomorskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (21,21,31,2,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (22,22,22,1,'Poland','Wojewodztwo Mazowieckie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (23,23,23,6,'Poland','Wojewodztwo Lubelskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (24,24,24,2,'Poland','Wojewodztwo Wielkopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (25,25,25,6,'Poland','Wojewodztwo Lodzkie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (26,26,26,8,'Poland','Wojewodztwo Malopolskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (27,27,27,3,'Poland','Wojewodztwo Zachodniopomorskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (28,28,28,6,'Poland','Wojewodztwo Dolnoslaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (29,29,29,7,'Poland','Wojewodztwo Slaskie');
INSERT INTO grant_assignments(assignment_id,grant_id,contractor_id,source_id,implementation_country,regional_authority) VALUES (30,30,30,4,'Poland','Wojewodztwo Kujawsko-Pomorskie');


CREATE TABLE signatories(
   signatory_id           INTEGER NOT NULL PRIMARY KEY,
   full_name              TEXT    NOT NULL,
   position               TEXT    NOT NULL,
   organization           TEXT    NOT NULL,
   email                  TEXT,
   phone                  TEXT    NOT NULL,
   authorization_level    TEXT    NOT NULL,
   digital_signature_hash TEXT    NOT NULL,
   is_active              INTEGER NOT NULL
);


INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (1,'AntiDemocracyAI','Chief Authorization Officer','EU Grant Management System',NULL,'','LEVEL_5','a3f5d8e9c2b1a0f7e6d4c3b2a1f0e9d8',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (2,'Jan Kowalski','Dyrektor Departamentu','Ministerstwo Funduszy i Polityki Regionalnej','j.kowalski@mfpr.gov.pl','+48 22 273 8000','LEVEL_3','b2e4f1a9d8c7b6a5f4e3d2c1b0a9f8e7',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (3,'Anna Nowak','Kierownik Wydzialu Grantow','Ministerstwo Cyfryzacji','a.nowak@mc.gov.pl','+48 22 250 3000','LEVEL_3','c1d3e5f7a9b0c2d4e6f8a0b1c3d5e7f9',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (4,'Piotr Wisniewski','Specjalista ds. Funduszy UE','NFOSiGW','p.wisniewski@nfosigw.gov.pl','+48 22 459 0000','LEVEL_2','d0e2f4a6b8c0d2e4f6a8b0c2d4e6f8a0',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (5,'Maria Lewandowska','Dyrektor Biura Projektow','PARP','m.lewandowska@parp.gov.pl','+48 22 432 8000','LEVEL_3','e9f1a3b5c7d9e0f2a4b6c8d0e2f4a6b8',0);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (6,'Krzysztof Dabrowski','Kierownik Departamentu Innowacji','Ministerstwo Rozwoju','k.dabrowski@mr.gov.pl','+48 22 273 7000','LEVEL_3','f8a0b2c4d6e8f0a1b3c5d7e9f1a3b5c7',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (7,'Magdalena Szymanska','Zastepca Dyrektora','Ministerstwo Klimatu i Srodowiska','m.szymanska@klimat.gov.pl','+48 22 369 2000','LEVEL_3','a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (8,'Tomasz Kaczmarek','Kierownik Wydzialu Infrastruktury','Ministerstwo Infrastruktury','t.kaczmarek@mi.gov.pl','+48 22 630 1000','LEVEL_2','b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (9,'Agnieszka Wojcik','Specjalista ds. Rozwoju Miejskiego','Ministerstwo Rozwoju i Technologii','a.wojcik@mrit.gov.pl','+48 22 273 8500','LEVEL_2','c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8',1);
INSERT INTO signatories(signatory_id,full_name,position,organization,email,phone,authorization_level,digital_signature_hash,is_active) VALUES (10,'Robert Adamczyk','Dyrektor Departamentu Spolecznego','Ministerstwo Rodziny','r.adamczyk@mrips.gov.pl','+48 22 461 6000','LEVEL_3','d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9',1);


CREATE TABLE grant_signatures(
   signature_id    INTEGER NOT NULL PRIMARY KEY,
   grant_id        INTEGER NOT NULL,
   signatory_id    INTEGER NOT NULL,
   signature_date  TEXT    NOT NULL,
   signature_type  TEXT    NOT NULL,
   is_verified     INTEGER NOT NULL
);


INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (1,1,1,'2025-11-15','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (2,2,1,'2025-11-20','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (3,3,1,'2025-11-25','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (4,4,1,'2025-12-01','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (5,5,1,'2025-12-05','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (6,6,1,'2025-12-08','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (7,7,3,'2025-05-10','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (8,8,6,'2025-08-15','Manual Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (9,9,2,'2025-09-20','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (10,10,4,'2025-01-01','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (11,11,1,'2025-11-18','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (12,12,1,'2025-11-22','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (13,13,1,'2025-11-28','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (14,14,1,'2025-12-03','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (15,15,1,'2025-12-07','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (16,16,1,'2025-12-10','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (17,17,4,'2025-06-15','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (18,18,6,'2025-03-20','Manual Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (19,19,4,'2025-08-10','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (20,20,8,'2025-10-05','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (21,21,1,'2025-11-17','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (22,22,2,'2025-11-23','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (23,23,10,'2025-12-02','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (24,24,3,'2025-12-06','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (25,25,10,'2025-12-09','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (26,26,9,'2025-09-12','Manual Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (27,27,4,'2025-07-20','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (28,28,2,'2025-10-15','Digital Signature',0);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (29,29,7,'2025-05-08','Digital Signature',1);
INSERT INTO grant_signatures(signature_id,grant_id,signatory_id,signature_date,signature_type,is_verified) VALUES (30,30,5,'2025-09-25','Digital Signature',0);
