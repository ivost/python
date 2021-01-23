import sys

_pv = sys.version_info
if _pv[0] == 3 and _pv[1] == 6:
    # if using py 3.6 - backport of 3.7 dataclasses
    from dataclasses import dataclass

@dataclass
class InventoryItem:
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand


if __name__ == '__main__':
    # print("python", sys.version_info)
    # python sys.version_info(major=3, minor=6, micro=9, releaselevel='final', serial=0)
    item = InventoryItem('pythons', 5, 2)
    print(f"total: {item.total_cost()}")

    item2 = InventoryItem('hammers', unit_price=10.49, quantity_on_hand=12)
    print(f"total: {item2.total_cost()}")