USE prestashop;
UPDATE `ps_shop_url` SET `domain` = 'localhost:8080', `domain_ssl` = 'localhost:18467' WHERE `ps_shop_url`.`id_shop_url` = 1;
