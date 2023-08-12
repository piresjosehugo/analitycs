/*/

Cleaning Data in SQL Queries

*/

Select *

From PortofolioProject.dbo.NashvilleHousing

--Change Date Format

Select SaleDateConverted, CONVERT(Date, SaleDate)

From PortofolioProject.dbo.NashvilleHousing

Update NashvilleHousing

SET SaleDate = CONVERT(Date, SaleDate)

ALTER TABLE NashvilleHousing
Add SaleDateConverted Date;

Update NashvilleHousing

SET SaleDateConverted = CONVERT(Date, SaleDate)

-- Populate Property Adress Data

Select PropertyAddress

From PortofolioProject.dbo.NashvilleHousing

--Where PropertyAddress is null

order by ParcelID

Select a.ParcelID, a.PropertyAddress, b.ParcelID, ISNULL(a.PropertyAddress, b.PropertyAddress)

From PortofolioProject.dbo.NashvilleHousing a
JOIN PortofolioProject.dbo.NashvilleHousing b
    on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null

Update a

SET PropertyAddress = ISNULL(a.PropertyAddress, b.PropertyAddress)
From PortofolioProject.dbo.NashvilleHousing a
JOIN PortofolioProject.dbo.NashvilleHousing b
    on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null

--Breaking out Address into Individual Columns (Adress, City, State)

Select PropertyAddress

From PortofolioProject.dbo.NashvilleHousing

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1) as Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress)) as Address

FROM PortofolioProject.dbo.NashvilleHousing

ALTER TABLE NashvilleHousing
Add PropertySlipAddress Nvarchar(225);

Update NashvilleHousing

SET PropertySlipAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1)

ALTER TABLE NashvilleHousing
Add PropertySlipCity Nvarchar(225);

Update NashvilleHousing

SET PropertySlipCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) +1, LEN(PropertyAddress))



Select *

From PortofolioProject.dbo.NashvilleHousing

Select OwnerAddress

From PortofolioProject.dbo.NashvilleHousing

SELECT 
PARSENAME(REPLACE(OwnerAddress, ',', '.'),3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'),2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)
FROM PortofolioProject.dbo.NashvilleHousing


ALTER TABLE NashvilleHousing
Add OwnerSlipAddress Nvarchar(225);

Update NashvilleHousing

SET OwnerSlipAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.'),3)

ALTER TABLE NashvilleHousing
Add OwnerSlipCity Nvarchar(225);

Update NashvilleHousing

SET OwnerSlipCity = PARSENAME(REPLACE(OwnerAddress, ',', '.'),2)

ALTER TABLE NashvilleHousing
Add OwnerSlipState Nvarchar(225);

Update NashvilleHousing

SET OwnerSlipState = PARSENAME(REPLACE(OwnerAddress, ',', '.'),1)

--Change Y and N to Yes and No in "Sold as Vacant" field

Select Distinct (SoldAsVacant), COUNT(SoldAsVacant)
From PortofolioProject.dbo.NashvilleHousing
Group by SoldAsVacant
order by 2

Select SoldAsVacant
, CASE when SoldAsVacant = 'Y' THEN 'Yes'
       when SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END
From PortofolioProject.dbo.NashvilleHousing

Update NashvilleHousing
SET SoldAsVacant = CASE when SoldAsVacant = 'Y' THEN 'Yes'
       when SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END

--Remove Duplicates

WITH RowNumCTE AS(
Select *,
     ROW_NUMBER() OVER (
	 PARTITION BY ParcelID,
                  PropertyAddress,
				  SalePrice,
				  SaleDate,
				  LegalReference
				  ORDER BY
				     UniqueID
					 ) row_num


From PortofolioProject.dbo.NashvilleHousing
--order by ParcelID
)

Select *
From RowNumCTE
Where row_num > 1
Order by PropertyAddress



Select *

From PortofolioProject.dbo.NashvilleHousing

--Delete Unused Colums

ALTER TABLE PortofolioProject.dbo.NashvilleHousing
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress

ALTER TABLE PortofolioProject.dbo.NashvilleHousing
DROP COLUMN SaleDate