<?php
/* Smarty version 3.1.39, created on 2021-11-04 18:47:53
  from '/var/www/html/admin-cinema/themes/new-theme/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.39',
  'unifunc' => 'content_61841cc9e005b4_96558778',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'ce510ab2c63eacb9e7e1cd02ab06c3cfac60be78' => 
    array (
      0 => '/var/www/html/admin-cinema/themes/new-theme/template/content.tpl',
      1 => 1633363913,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_61841cc9e005b4_96558778 (Smarty_Internal_Template $_smarty_tpl) {
?>
<div id="ajax_confirmation" class="alert alert-success" style="display: none;"></div>


<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
  <?php echo $_smarty_tpl->tpl_vars['content']->value;?>

<?php }
}
}