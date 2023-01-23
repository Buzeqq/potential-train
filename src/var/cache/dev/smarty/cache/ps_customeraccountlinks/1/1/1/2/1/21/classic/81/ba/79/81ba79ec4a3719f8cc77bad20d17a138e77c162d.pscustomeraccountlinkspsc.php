<?php
/* Smarty version 4.2.1, created on 2023-01-23 23:00:29
  from 'module:pscustomeraccountlinkspsc' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_63cf037d58bc87_69070595',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '42f9461127ce7396a601c2484841253ea5ba658f' => 
    array (
      0 => 'module:pscustomeraccountlinkspsc',
      1 => 1671890849,
      2 => 'module',
    ),
  ),
  'cache_lifetime' => 31536000,
),true)) {
function content_63cf037d58bc87_69070595 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->smarty->ext->_tplFunction->registerTplFunctions($_smarty_tpl, array (
  'renderLogo' => 
  array (
    'compiled_filepath' => '/var/www/html/var/cache/dev/smarty/compile/classiclayouts_layout_full_width_tpl/d2/2d/85/d22d851f6d7c12eb35c1c34c8e84baa801a8cea2_2.file.helpers.tpl.php',
    'uid' => 'd22d851f6d7c12eb35c1c34c8e84baa801a8cea2',
    'call_name' => 'smarty_template_function_renderLogo_162145474263cf037d393b17_70649811',
  ),
));
?><!-- begin /var/www/html/themes/classic/modules/ps_customeraccountlinks/ps_customeraccountlinks.tpl -->
<div id="block_myaccount_infos" class="col-md-3 links wrapper">
  <p class="h3 myaccount-title hidden-sm-down">
    <a class="text-uppercase" href="https://localhost:4433/index.php?controller=my-account" rel="nofollow">
      Your account
    </a>
  </p>
  <div class="title clearfix hidden-md-up" data-target="#footer_account_list" data-toggle="collapse">
    <span class="h3">Your account</span>
    <span class="float-xs-right">
      <span class="navbar-toggler collapse-icons">
        <i class="material-icons add">&#xE313;</i>
        <i class="material-icons remove">&#xE316;</i>
      </span>
    </span>
  </div>
  <ul class="account-list collapse" id="footer_account_list">
            <li><a href="https://localhost:4433/index.php?controller=guest-tracking" title="Order tracking" rel="nofollow">Order tracking</a></li>
        <li><a href="https://localhost:4433/index.php?controller=my-account" title="Log in to your customer account" rel="nofollow">Sign in</a></li>
        <li><a href="https://localhost:4433/index.php?controller=registration" title="Create account" rel="nofollow">Create account</a></li>
        
<!-- begin module:blockwishlist/views/templates/hook/account/myaccount-block.tpl -->
<!-- begin /var/www/html/modules/blockwishlist/views/templates/hook/account/myaccount-block.tpl -->
<!-- end /var/www/html/modules/blockwishlist/views/templates/hook/account/myaccount-block.tpl -->
<!-- end module:blockwishlist/views/templates/hook/account/myaccount-block.tpl -->

<!-- begin /var/www/html/themes/classic/modules/ps_emailalerts/views/templates/hook/my-account-footer.tpl -->
<li>
  <a href="//localhost:4433/index.php?fc=module&module=ps_emailalerts&controller=account&id_lang=2" title="My alerts">
    My alerts
  </a>
</li>

<!-- end /var/www/html/themes/classic/modules/ps_emailalerts/views/templates/hook/my-account-footer.tpl -->

       
	</ul>
</div>
<!-- end /var/www/html/themes/classic/modules/ps_customeraccountlinks/ps_customeraccountlinks.tpl --><?php }
}
