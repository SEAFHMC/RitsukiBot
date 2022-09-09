from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class KeyImage(BaseModel):
    type: str
    url: str


class Seller(BaseModel):
    id: str
    name: str


class Item(BaseModel):
    id: str
    namespace: str


class CustomAttribute(BaseModel):
    key: str
    value: str


class Category(BaseModel):
    path: str


class Tag(BaseModel):
    id: str


class Mapping(BaseModel):
    pageSlug: str
    pageType: str


class CatalogNs(BaseModel):
    mappings: List[Mapping]


class OfferMapping(BaseModel):
    pageSlug: str
    pageType: str


class CurrencyInfo(BaseModel):
    decimals: int


class FmtPrice(BaseModel):
    originalPrice: str
    discountPrice: str
    intermediatePrice: str


class TotalPrice(BaseModel):
    discountPrice: int
    originalPrice: int
    voucherDiscount: int
    discount: int
    currencyCode: str
    currencyInfo: CurrencyInfo
    fmtPrice: FmtPrice


class DiscountSetting(BaseModel):
    discountType: str


class AppliedRule(BaseModel):
    id: str
    endDate: str
    discountSetting: DiscountSetting


class LineOffer(BaseModel):
    appliedRules: List[AppliedRule]


class Price(BaseModel):
    totalPrice: TotalPrice
    lineOffers: List[LineOffer]


class DiscountSetting1(BaseModel):
    discountType: str
    discountPercentage: int


class PromotionalOffer1(BaseModel):
    startDate: str
    endDate: str
    discountSetting: DiscountSetting1


class PromotionalOffer(BaseModel):
    promotionalOffers: List[PromotionalOffer1]


class DiscountSetting2(BaseModel):
    discountType: str
    discountPercentage: int


class PromotionalOffer2(BaseModel):
    startDate: str
    endDate: str
    discountSetting: DiscountSetting2


class UpcomingPromotionalOffer(BaseModel):
    promotionalOffers: List[PromotionalOffer2]


class Promotion(BaseModel):
    promotionalOffers: List[PromotionalOffer]
    upcomingPromotionalOffers: List[UpcomingPromotionalOffer]


class Element(BaseModel):
    title: str
    id: str
    namespace: str
    description: str
    effectiveDate: str
    offerType: str
    expiryDate: Optional[str]
    status: str
    isCodeRedemptionOnly: bool
    keyImages: List[KeyImage]
    seller: Seller
    productSlug: Optional[str]
    urlSlug: str
    url: Any
    items: List[Item]
    customAttributes: List[CustomAttribute]
    categories: List[Category]
    tags: List[Tag]
    catalogNs: CatalogNs
    offerMappings: List[OfferMapping]
    price: Price
    promotions: Optional[Promotion]


class Paging(BaseModel):
    count: int
    total: int


class SearchStore(BaseModel):
    elements: List[Element]
    paging: Paging


class Catalog(BaseModel):
    searchStore: SearchStore


class Data(BaseModel):
    Catalog: Catalog


class Model(BaseModel):
    data: Data
    extensions: Dict[str, Any]
