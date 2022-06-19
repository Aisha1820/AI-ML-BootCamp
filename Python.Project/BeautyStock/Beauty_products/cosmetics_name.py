def shows(cosmetics_name):
    cosmetics_list=[]
    if  cosmetics_name=="hair_fall":
        
        product_price_dict={'hair_oil':['100RS','130RS','250RS','320RS','500RS'],
                            'shampoo': ['180RS', '230RS', '310RS', '420RS', '580RS'],
                            'conditioner': ['100RS', '130RS', '250RS', '320RS', '500RS'],
                            'hair_jell': ['100RS', '130RS', '250RS', '320RS', '500RS'],
                            }

        return product_price_dict


    elif cosmetics_name=="makeup":
        cosmetics_list=['foundation','powder','lipstick','mascara']
        product_list_dict={'foundation':['liquid','dry','powder','jell'],
                           'powder':['white_tone','fruit','sandal_wood','ponds'],
                           'lipstick':['red','pink','purple','blue'],
                           'mascara':['lash','curl','waterproof','fiber']
                           }
        product_price_dict={'foundation':['150RS','220RS','280RS','300RS'],
                       'powder':['260RS','190RS','230RS','390RS'],
                       'lipstick':['120RS','180RS','230RS','80RS'],
                       'mascara':['120RS','230RS','300RS','280RS']
                       }
        return product_price_dict
    elif cosmetics_name=="face_wash":
        cosmetics_list=['fruit','aloevera','neem','teatree']
        product_list_dict={'fruit':['25ml','50ml','100ml','250ml','500ml'],
                           'aloevera':['25ml','50ml','100ml','250ml','500ml'],
                           'neem':['25ml','50ml','100ml','250ml','500ml'],
                           'teatree':['25ml','50ml','100ml','250ml','500ml']
                           }
        product_price_dict={'fruit':['50RS','70RS','100RS','150RS','230RS'],
                       'aloevera':['70RS','120RS','230RS','450RS','620RS'],
                       'neem':['50RS','70RS','120RS','180RS','250RS'],
                       'teatree':['95RS','160RS','270RS','360RS','520RS']
                       }
        return product_price_dict
        

    elif cosmetics_name == "peeloff_mask":
        cosmetics_list = ['fruit', 'aloevera', 'neem', 'teatree']
        product_list_dict = {'fruit': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'aloevera': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'neem': ['25ml', '50ml', '100ml', '250ml', '500ml'],
                             'teatree': ['25ml', '50ml', '100ml', '250ml', '500ml']
                             }
        product_price_dict={'fruit':['50RS','70RS','100RS','150RS','230RS'],
                       'aloevera':['70RS','120RS','230RS','450RS','620RS'],
                       'neem':['50RS','70RS','120RS','180RS','250RS'],
                       'teatree':['95RS','160RS','270RS','360RS','520RS']
                      }

        return product_price_dict



