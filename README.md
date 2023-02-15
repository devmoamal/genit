Genit Library<a name="TOP"></a>
===================

## Install Genit ##

    $ pip install genit
    
## How it Works ? ##

### 1 -  Random String ###

The Gstr function use "abcdefghijklmnopqrstuvwxyz"

You can aslo add your own characters form add_characters parameter

    import genit
    
    # 10 = length of generation
    # "" = If you want to use your own characters like "$^&@!*-+±§"
       
    random_string = genit.Gstr(10, "")
    print(random_string)
    
    # output "opemauivye"
    
### 2 -  Random Integer ###

the Gint function use "1234567890"

    import genit

    # 15 = length of generation
    
    random_integer = genit.Gint(15)
    print(random_integer)

    # output "483226821395342"
    
### 3 -  Random All ###

The Gall function use "abcdefghijklmnopqrstuvwxyz1234567890"

You can aslo add your own characters form add_characters parameter

    import genit

    # 8 = length of generation
    
    random_all = genit.Gall(8)
    print(random_all)

    # output "kf1a8s46"

### 4 -  Random Special ###

The Gspecial function use your own characters

    import genit

    # 8 = length of generation
    # "abc" = my own characters
    
    random_special = genit.Gspecial(8, "abc")
    print(random_special)

    # output "abcccbab"
