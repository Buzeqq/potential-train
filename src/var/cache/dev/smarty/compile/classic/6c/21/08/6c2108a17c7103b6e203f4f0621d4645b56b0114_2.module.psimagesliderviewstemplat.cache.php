<?php
/* Smarty version 4.2.1, created on 2023-01-23 22:46:47
  from 'module:psimagesliderviewstemplat' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '4.2.1',
  'unifunc' => 'content_63cf004780f329_02864917',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '6c2108a17c7103b6e203f4f0621d4645b56b0114' => 
    array (
      0 => 'module:psimagesliderviewstemplat',
      1 => 1671890849,
      2 => 'module',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_63cf004780f329_02864917 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->compiled->nocache_hash = '163072998763cf00477b6674_72435987';
?>
<!-- begin /var/www/html/themes/classic/modules/ps_imageslider/views/templates/hook/slider.tpl -->
<?php if ($_smarty_tpl->tpl_vars['homeslider']->value['slides']) {?>
  <div id="carousel" data-ride="carousel" class="carousel slide" data-interval="<?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['homeslider']->value['speed'], ENT_QUOTES, 'UTF-8');?>
" data-wrap="<?php echo htmlspecialchars((string) (string)$_smarty_tpl->tpl_vars['homeslider']->value['wrap'], ENT_QUOTES, 'UTF-8');?>
" data-pause="<?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['homeslider']->value['pause'], ENT_QUOTES, 'UTF-8');?>
" data-touch="true">
    <ol class="carousel-indicators">
      <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['homeslider']->value['slides'], 'slide', false, 'idxSlide', 'homeslider', array (
  'first' => true,
  'index' => true,
));
$_smarty_tpl->tpl_vars['slide']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['idxSlide']->value => $_smarty_tpl->tpl_vars['slide']->value) {
$_smarty_tpl->tpl_vars['slide']->do_else = false;
$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['index']++;
$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first'] = !$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['index'];
?>
      <li data-target="#carousel" data-slide-to="<?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['idxSlide']->value, ENT_QUOTES, 'UTF-8');?>
"<?php if ($_smarty_tpl->tpl_vars['idxSlide']->value == 0) {?> class="active"<?php }?>></li>
      <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
    </ol>
    <ul class="carousel-inner" role="listbox" aria-label="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Carousel container','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
">
      <?php
$_from = $_smarty_tpl->smarty->ext->_foreach->init($_smarty_tpl, $_smarty_tpl->tpl_vars['homeslider']->value['slides'], 'slide', false, NULL, 'homeslider', array (
  'first' => true,
  'index' => true,
));
$_smarty_tpl->tpl_vars['slide']->do_else = true;
if ($_from !== null) foreach ($_from as $_smarty_tpl->tpl_vars['slide']->value) {
$_smarty_tpl->tpl_vars['slide']->do_else = false;
$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['index']++;
$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first'] = !$_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['index'];
?>
        <li class="carousel-item <?php if ((isset($_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first']) ? $_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first'] : null)) {?>active<?php }?>" role="option" aria-hidden="<?php if ((isset($_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first']) ? $_smarty_tpl->tpl_vars['__smarty_foreach_homeslider']->value['first'] : null)) {?>false<?php } else { ?>true<?php }?>">
          <?php if (!empty($_smarty_tpl->tpl_vars['slide']->value['url'])) {?><a href="<?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['slide']->value['url'], ENT_QUOTES, 'UTF-8');?>
"><?php }?>
            <figure>
              <img src="<?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['slide']->value['image_url'], ENT_QUOTES, 'UTF-8');?>
" alt="<?php echo htmlspecialchars((string) call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['slide']->value['legend'] )), ENT_QUOTES, 'UTF-8');?>
" loading="lazy" width="1110" height="340">
              <?php if ($_smarty_tpl->tpl_vars['slide']->value['title'] || $_smarty_tpl->tpl_vars['slide']->value['description']) {?>
                <figcaption class="caption">
                  <h2 class="display-1 text-uppercase"><?php echo htmlspecialchars((string) $_smarty_tpl->tpl_vars['slide']->value['title'], ENT_QUOTES, 'UTF-8');?>
</h2>
                  <div class="caption-description"><?php echo $_smarty_tpl->tpl_vars['slide']->value['description'];?>
</div>
                </figcaption>
              <?php }?>
            </figure>
          <?php if (!empty($_smarty_tpl->tpl_vars['slide']->value['url'])) {?></a><?php }?>
        </li>
      <?php
}
$_smarty_tpl->smarty->ext->_foreach->restore($_smarty_tpl, 1);?>
    </ul>
    <div class="direction" aria-label="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Carousel buttons','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
">
      <a class="left carousel-control" href="#carousel" role="button" data-slide="prev" aria-label="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Previous','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
">
        <span class="icon-prev hidden-xs" aria-hidden="true">
          <i class="material-icons">&#xE5CB;</i>
        </span>
      </a>
      <a class="right carousel-control" href="#carousel" role="button" data-slide="next" aria-label="<?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Next','d'=>'Shop.Theme.Global'),$_smarty_tpl ) );?>
">
        <span class="icon-next" aria-hidden="true">
          <i class="material-icons">&#xE5CC;</i>
        </span>
      </a>
    </div>
  </div>
<?php }?>
<!-- end /var/www/html/themes/classic/modules/ps_imageslider/views/templates/hook/slider.tpl --><?php }
}
