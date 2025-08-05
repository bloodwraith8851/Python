"""
**Difficulty**: Intermediate  
**Time**: 45-60 minutes  
**Concepts**: Nested dictionaries, data validation, calculations

### Project Description
Build a restaurant ordering system where customers can view the menu, place orders, modify orders, and calculate bills with tax and tip.

### Requirements
- Display categorized menu with prices
- Take customer orders
- Modify existing orders
- Calculate subtotal, tax, tip, and total
- Show order summary
"""
# Restaurant menu data structure
MENU = {
    "appetizers": {
        "Buffalo Wings": 8.99,
        "Mozzarella Sticks": 6.99,
        "Nachos": 9.99,
        "Garlic Bread": 4.99
    },
    "main_courses": {
        "Grilled Chicken": 15.99,
        "Beef Burger": 12.99,
        "Salmon": 18.99,
        "Vegetarian Pasta": 11.99,
        "Steak": 24.99
    },
    "desserts": {
        "Chocolate Cake": 6.99,
        "Ice Cream": 4.99,
        "Apple Pie": 5.99,
        "Cheesecake": 7.99
    },
    "beverages": {
        "Soda": 2.99,
        "Coffee": 3.99,
        "Juice": 3.49,
        "Water": 1.99
    }
}

TAX_RATE = 0.08  # 8% tax
DEFAULT_TIP_RATE = 0.15  # 15% tip

class RestaurantOrderSystem:
    def __init__(self):
        self.current_order = {}
        self.order_total = 0.0
    
    def display_menu(self):
        """Display the full menu with categories and prices"""
        # TODO: Implement menu display
        pass
    
    def add_item_to_order(self):
        """Add an item to the current order"""
        # TODO: Implement adding items
        pass
    
    def modify_order(self):
        """Modify quantity of items in the order"""
        # TODO: Implement order modification
        pass
    
    def remove_item_from_order(self):
        """Remove an item from the order"""
        # TODO: Implement item removal
        pass
    
    def calculate_bill(self):
        """Calculate and display the final bill"""
        # TODO: Implement bill calculation
        pass
    
    def display_order_summary(self):
        """Show current order with quantities and prices"""
        # TODO: Implement order summary
        pass
    
    def run_restaurant_system(self):
        """Main program loop"""
        print("🍽️  Welcome to Python Restaurant! 🍽️")
        
        while True:
            print("\n" + "="*40)
            print("1. View Menu")
            print("2. Add Item to Order")
            print("3. View Current Order")
            print("4. Modify Order")
            print("5. Remove Item from Order")
            print("6. Calculate Final Bill")
            print("7. Exit")
            print("="*40)
            
            choice = input("Select an option (1-7): ").strip()
            
            # TODO: Implement menu choices
            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.add_item_to_order()
            elif choice == '3':
                self.display_order_summary()
            elif choice == '4':
                self.modify_order()
            elif choice == '5':
                self.remove_item_from_order()
            elif choice == '6':
                self.calculate_bill()
            elif choice == '7':
                print("Thank you for dining with us! 👋")
                break
            else:
                print("❌ Invalid choice. Please try again.")

# Helper functions
def find_item_in_menu(item_name):
    """Find an item in the menu and return its category and price"""
    # TODO: Implement item search
    pass

def get_valid_quantity():
    """Get a valid quantity from user input"""
    # TODO: Implement quantity validation
    pass

if __name__ == "__main__":
    restaurant = RestaurantOrderSystem()
    restaurant.run_restaurant_system()