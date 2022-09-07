고객(Customers)의 이름과 국가를 조회
SELECT CustomerName, Country FROM Customers;

고객(Customers)의 정보 전체 조회
SELECT * FROM Customers;

고객(Customers)의 국가(Country) 목록 조회 (중복 x)
SELECT DISTINCT Country FROM Customers;

국가(Country)가 France인 고객 (Customers) 조회
SELECT * FROM Customers WHERE Country='France';


고객(Customers) 테이블에서
Q. 이름(ContactName) 이 'Mar' 로 시작하는 직원 조회
SELECT * 
FROM Customers
WHERE ContactName LIKE 'Mar%';

Q. 이름(ContactName) 이 'et' 로 끝나는 직원 조회
SELECT * 
FROM Customers
WHERE ContactName LIKE '%et';


국가(Country)가 France이고 
이름(ContactName)이 'La'로 시작하는 고객(Customers) 조회
SELECT *
FROM Customers
WHERE Country='France' AND ContactName LIKE 'La%';


국가(Country)가 France이거나
이름(ContactName)이 'La'로 시작하는 고객(Customers) 조회
SELECT *
FROM Customers
WHERE Country='France' OR ContactName LIKE 'La%';

국가(Country)가 France가 아닌
고객(Customers) 조회
SELECT *
FROM Customers
WHERE NOT Country='France';

국가(Country)가 France 혹은 Spain에 사는
고객(Customers) 조회
SELECT *
FROM Customers
WHERE Country IN ('France', 'Spain');

가격(Price)이 15에서 20 사이인 상품(Products) 조회
SELECT *
FROM Products
WHERE Price BETWEEN 15 AND 20;

우편번호(PostalCode) 가 NULL 인 고객(Customers) 조회
SELECT PostalCode
FROM Customers
WHERE PostalCode IS NULL

우편번호(PostalCode) 가 NULL 이 아닌 고객(Customers) 조회
SELECT PostalCode
FROM Customers
WHERE PostalCode IS NOT NULL

우편번호가 공백인 고객을 NULL로 수정 후 다시 조회
UPDATE Customers
SET PostalCode=NULL
WHERE PostalCode='';

고객이름(CustomerName) 오름차순 조회 (Customers)
SELECT *
FROM Customers
ORDER BY CustomerName ASC;

상품가격(Price) 내림차순 조회 (Products)
SELECT *
FROM Products
ORDER BY Price DESC;

10명만 조회 (Customers)
SELECT *
FROM Customers
LIMIT 10;

그 다음 10명 조회 (Customers)
SELECT *
FROM Customers
LIMIT 10
OFFSET 10;

-- LIMIT 활용 (OFFSET, LIMIT)
SELECT *
FROM Customers
LIMIT 40, 10;


상품가격(Price) 이 30 미만이면 '저', 30 ~ 50이면 '중', 
50 초과는 '고'로 조회 (Products)
SELECT 
    CASE
        WHEN Price < 30 THEN '저'
        WHEN Price <= 50 THEN '중'
        ELSE '고'
    END
FROM Products;

위 조회한 CASE의 이름을 'Level'로 바꿔주세요
SELECT Price,
    CASE
        WHEN Price < 30 THEN '저'
        WHEN Price <= 50 THEN '중'
        ELSE '고'
    END AS 'Level'
FROM Products;

국가(Country)가 France에 사는 고객(Customers) 수 조회
SELECT Country, COUNT(CustomerID)
FROM Customers
WHERE Country='France';

전체 상품(Products)의 평균 가격(Price) 계산
SELECT AVG(Price)
FROM Products;

주문상품 수량(Qunatity) 합계 계산
SELECT SUM(Quantity)
FROM OrderDetails;

가격(Price) 최소값 조회 (Products)
SELECT MIN(Price)
FROM Products;

-- 가격(Price) 최대값 조회 (Products)
SELECT MAX(Price)
FROM Products;


-- 국가(Country) 별 고객수 조회 고객수 기준 오름차순 (Customers)
SELECT Country, COUNT(CustomerID) AS TotalCustomer
FROM Customers
GROUP BY Country
ORDER BY TotalCustomer ASC;

-- 국가(Country) 별, 도시(City) 별 고객수 조회 고객수 기준 내림차순 (Customers)
SELECT Country, City, COUNT(CustomerID) AS TotalCustomer
FROM Customers
GROUP BY Country, City
ORDER BY TotalCustomer DESC;

-- 국가(Country) 별 고객수를 조회하고 그 중 5명 초과인 국가만 조회 
-- 고객수 기준 내림차순 (Customers)
SELECT Country, COUNT(CustomerID) AS TotalCustomer
FROM Customers
GROUP BY Country
HAVING TotalCustomer > 5
ORDER BY TotalCustomer DESC;

-- 직원(Employees) 중 이름(LastName)이 'King'인 직원의 
-- 이름과 생일(BirthDate)과 노트(Notes)를 조회해주세요
SELECT FirstName, LastName, BirthDate, Notes
FROM Employees
WHERE LastName='King';


-- 상품(Products) 중 상품명(ProductName)이 'C'로 시작하고 
-- 가격(Price)이 20보다 큰 상품의 상품명과 가격을 가격이 비싼순으로 조회해주세요
SELECT ProductName, Price
FROM Products
WHERE ProductName LIKE 'C%' AND Price > 20
ORDER BY Price DESC;

-- 상품(Products)의 카테고리아이디(CategoryID) 별로 
-- 상품가격의 합, 가장 비싼 상품 가격, 가장 저렴한 상품 가격을 구하세요
SELECT CategoryID, SUM(Price), MAX(Price), MIN(Price)
FROM Products
GROUP BY CategoryID;

-- 상품(Products)의 카테고리아이디(CategoryID) 별로 
-- 상품개수와 상품개수가 10개가 넘을경우 많음 아니면 적음이 표시되어있는 
-- 칼럼을 하나 추가하고 상품수가 많은 순서대로 조회해주세요
SELECT CategoryID, COUNT(ProductID) AS Quantity, 
    CASE
        WHEN COUNT(ProductID) > 10 THEN '많음'
        ELSE '적음'
    END
FROM Products
GROUP BY CategoryID
ORDER BY Quantity DESC;

-- 고객(Customers)의 국가(Country) 별 고객수와 
-- 백분위(국가별고객수/전체고객수*100)을 구하세요
SELECT Country, COUNT(CustomerID) AS CountryCustomer,
    -- 전체 고객수를 구하는 서브쿼리
    (SELECT COUNT(CustomerID) FROM Customers) AS TotalCustomer,
    -- 백분위를 구하는 곳 (국가별 고객수 * 100 / 전체 고객수)
    (COUNT(CustomerID) * 100 / (SELECT COUNT(CustomerID) FROM Customers))
        AS Percentile
FROM Customers
GROUP BY Country;