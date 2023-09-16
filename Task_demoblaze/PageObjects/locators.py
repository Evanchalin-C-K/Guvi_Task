class Locators:
    # Home Page
    logo_loc = "//a/img"
    navigation_menu_loc = "//div[@class='navbar-collapse']//li/a"
    featured_products_loc = "//div[@class='carousel-inner']//img"
    # SignUp
    sign_up = "//a[text()='Sign up']"
    username_loc = "//input[@id='sign-username']"
    password_loc = "//input[@id='sign-password']"
    sign_up_btn_loc = "//button[contains(text(), 'Sign up')]"
    # Login
    login_loc = "login2"  # ID
    login_username = "loginusername"  # ID
    login_password = "loginpassword"  # ID
    login_btn = "//button[contains(text(), 'Log in')]"
    # Add to Cart
    # laptop_loc = "div>div>div>a:nth-child(3)"  # CSS selector
    laptop_loc = "Laptops"
    macbook_pro = "//a[contains(text(), 'MacBook Pro')]"
    add_to_cart = "//a[contains(text(), 'Add to cart')]"
    # Cart - Purchase
    cart_loc = "ul>li:nth-child(4)>a"  # CSS selector
    place_order = "//button[contains(text(), 'Place Order')]"
    name_loc = "//input[@id='name']"
    country_loc = "//input[@id='country']"
    city_loc = "//input[@id='city']"
    credit_card_loc = "//input[@id='card']"
    month_loc = "//input[@id='month']"
    year_loc = "//input[@id='year']"
    purchase_loc = "//button[contains(text(), 'Purchase')]"
    ok_btn = "//button[contains(text(), 'OK')]"
    # Logout
    logout_btn = "Log out"  # LINK TEXT
