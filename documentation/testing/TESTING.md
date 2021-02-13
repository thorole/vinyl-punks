# Manually tested actions

## Navigation and header

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
Nav links (filters)|click|Only albums matching the filter is displayed| |x
Sort select|click|Sorts current selection of albums according to chosen sorting method| |x
Logo|click|Take user to landing page/display all albums| |x
Search field|enter keyword + click|Display results| |x
My Account icon|click|Display dropdown| |x
My account links|click|Take user to correct section| |x
Cart icon|click|Display cart preview (except when viewing cart page and on small screens)| |x
Delete icon in cart preview|click|Removes album from cart| |x*


## Cart

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
"Buy"-button (all albums- and album details view)|click|Add album to cart and display toast| |x
Delete icon in cart|click|Removes album from cart| |x
Quantity input in cart|enter number/click up/down buttons|Immediately update cart | |x
Quantity input in cart|enter invalid value (none integer 0-10)|Display helpful error message| |x


**Item**|**Action**|**Expected result **|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
Checkout button (cart preview/cart)|click|Go to checkout page| |x
Edit Cart button (checkout/cart preview)|click|Go to cart| |x
Shipping form|submit w/ empty required fields|No submit| |x
Shipping form|submit w/ content in required fields|Submit| |x
Card input|invalid card details|error message| |x
Card input|valid card details|loader -> success page| |x

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
New review form|submit w/ empty required fields|No submit| |x
New review form|submit w/ content in required fields|Submit| |x
Edit review icon|click|open editable review form| |x
Review save button|click|close editable review form and display updated values| |x
Review delete button|click|Display delete-modal. If the user choose delete, review and rating is deleted| |x

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
Delete album button|click|Display delete-modal. If user choose delete, album, reviews and ratings are deleted.| |x
Edit album button|click|Take user to album edit page| |x
Album save button |click|Go to album details w/ updated details| |x
Add tracks button|click|Go to album details w/ updated tracklist| |x

**Item**|**Action**|**Expected result**|**Fail**|**Pass**
:-----:|:-----:|:-----:|:-----:|:-----:
Register form|submit|Send confirmation email| |x
Login form|submit|Enable profile page and ability to write/edit/delete reviews and ratings| |x
Log out button|click|Disable profile page and ability to write/edit/delete reviews and ratings| |x





