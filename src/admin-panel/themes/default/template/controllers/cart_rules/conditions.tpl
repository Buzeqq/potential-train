{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Open Software License (OSL 3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/OSL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/OSL-3.0 Open Software License (OSL 3.0)
 *}
<div class="form-group">
	<label class="control-label col-lg-3">
		<span class="label-tooltip" data-toggle="tooltip"
			title="{l|escape s='Optional: The cart rule will be available to everyone if you leave this field blank.' d='Admin.Catalog.Help'}">
			{l s='Limit to a single customer' d='Admin.Catalog.Feature'}
		</span>
	</label>
	<div class="col-lg-9">
		<div class="input-group col-lg-12">
			<span class="input-group-addon"><i class="icon-user"></i></span>
			<input type="hidden" id="id_customer" name="id_customer" value="{$currentTab->getFieldValue($currentObject, 'id_customer')|intval}" />
			<input type="text" id="customerFilter" class="input-xlarge" name="customerFilter" value="{if $customerFilter}{$customerFilter|escape:'html':'UTF-8'}{elseif isset($smarty.post.customerFilter)}{$smarty.post.customerFilter|escape}{/if}" />
			<span class="input-group-addon"><i class="icon-search"></i></span>
		</div>
	</div>
</div>

<div class="form-group">
	<label class="control-label col-lg-3">
		<span class="label-tooltip" data-toggle="tooltip"
			title="{l|escape s='The default period is one month.' d='Admin.Catalog.Help'}">
			{l s='Valid' d='Admin.Catalog.Feature'}
		</span>
	</label>
	<div class="col-lg-9">
		<div class="row">
			<div class="col-lg-6">
				<div class="input-group">
					<span class="input-group-addon">{l s='From' d='Admin.Global'}</span>
					<input type="text" class="datepicker input-medium" name="date_from"
					value="{if $currentTab->getFieldValue($currentObject, 'date_from')}{$currentTab->getFieldValue($currentObject, 'date_from')|escape}{else}{$defaultDateFrom}{/if}" />
					<span class="input-group-addon"><i class="icon-calendar-empty"></i></span>
				</div>
			</div>
			<div class="col-lg-6">
				<div class="input-group">
					<span class="input-group-addon">{l s='To' d='Admin.Global'}</span>
					<input type="text" class="datepicker input-medium" name="date_to"
					value="{if $currentTab->getFieldValue($currentObject, 'date_to')}{$currentTab->getFieldValue($currentObject, 'date_to')|escape}{else}{$defaultDateTo}{/if}" />
					<span class="input-group-addon"><i class="icon-calendar-empty"></i></span>
				</div>
			</div>
		</div>
	</div>
</div>

<div class="form-group">
	<label class="control-label col-lg-3">
		<span class="label-tooltip" data-toggle="tooltip"
			title="{l|escape s='You can choose a minimum amount for the cart either with or without the taxes and shipping.' d='Admin.Catalog.Help'}">
			{l s='Minimum amount' d='Admin.Catalog.Feature'}
		</span>
	</label>
	<div class="col-lg-9">
		<div class="row">
			<div class="col-lg-3">
				<input type="text" name="minimum_amount" value="{$currentTab->getFieldValue($currentObject, 'minimum_amount')|floatval}" />
			</div>
			<div class="col-lg-2">
				<select name="minimum_amount_currency">
				{foreach from=$currencies item='currency'}
					<option value="{$currency.id_currency|intval}"
					{if $currentTab->getFieldValue($currentObject, 'minimum_amount_currency') == $currency.id_currency
						|| (!$currentTab->getFieldValue($currentObject, 'minimum_amount_currency') && $currency.id_currency == $defaultCurrency)}
						selected="selected"
					{/if}
					>
						{$currency.iso_code}
					</option>
				{/foreach}
				</select>
			</div>
			<div class="col-lg-3">
				<select name="minimum_amount_tax">
					<option value="0" {if $currentTab->getFieldValue($currentObject, 'minimum_amount_tax') === '0'}selected="selected"{/if}>{l s='Tax excluded' d='Admin.Global'}</option>
					<option value="1" {if $currentTab->getFieldValue($currentObject, 'minimum_amount_tax') === '1' || $currentTab->getFieldValue($currentObject, 'minimum_amount_tax') === false}selected="selected"{/if}>{l s='Tax included' d='Admin.Global'}</option>
				</select>
			</div>
			<div class="col-lg-4">
				<select name="minimum_amount_shipping">
					<option value="0" {if $currentTab->getFieldValue($currentObject, 'minimum_amount_shipping') === '0'}selected="selected"{/if}>{l s='Shipping excluded' d='Admin.Catalog.Feature'}</option>
					<option value="1" {if $currentTab->getFieldValue($currentObject, 'minimum_amount_shipping') === '1'}selected="selected"{/if}>{l s='Shipping included' d='Admin.Catalog.Feature'}</option>
				</select>
			</div>
		</div>
	</div>
</div>

<div class="form-group">
	<label class="control-label col-lg-3">
		<span class="label-tooltip" data-toggle="tooltip"
			title="{l|escape s='The cart rule will be applied to the first "X" customers only.' d='Admin.Catalog.Help'}">
			{l s='Total available' d='Admin.Catalog.Feature'}
		</span>
	</label>
	<div class="col-lg-9">
		<input class="form-control" type="text" name="quantity" value="{$currentTab->getFieldValue($currentObject, 'quantity')|intval}" />
	</div>
</div>

<div class="form-group">
	<label class="control-label col-lg-3">
		<span class="label-tooltip" data-toggle="tooltip"
			title="{l|escape s='A customer will only be able to use the cart rule "X" time(s).' d='Admin.Catalog.Help'}">
			{l s='Total available for each user' d='Admin.Catalog.Feature'}
		</span>
	</label>
	<div class="col-lg-9">
		<input class="form-control" type="text" name="quantity_per_user" value="{$currentTab->getFieldValue($currentObject, 'quantity_per_user')|intval}" />
	</div>
</div>



<div class="form-group">
	<label class="control-label col-lg-3">
		{l s='Restrictions' d='Admin.Catalog.Feature'}
	</label>
	<div class="col-lg-9">
		{if ($countries.unselected|@count) + ($countries.selected|@count) > 1}
			<p class="checkbox">
				<label>
					<input type="checkbox" id="country_restriction" name="country_restriction" value="1" {if $countries.unselected|@count}checked="checked"{/if} />
					{l s='Country selection' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<span class="help-block">{l s='This restriction applies to the country of delivery.' d='Admin.Catalog.Help'}</span>
			<div id="country_restriction_div">
				<br />
				<table class="table">
					<tr>
						<td>
							<p>{l s='Unselected countries' d='Admin.Catalog.Feature'}</p>
							<select id="country_select_1" multiple>
								{foreach from=$countries.unselected item='country'}
									<option value="{$country.id_country|intval}">&nbsp;{$country.name|escape}</option>
								{/foreach}
							</select>
							<a id="country_select_add" class="btn  btn-default btn-block clearfix">{l s='Add' d='Admin.Actions'} <i class="icon-arrow-right"></i></a>
						</td>
						<td>
							<p>{l s='Selected countries' d='Admin.Catalog.Feature'}</p>
							<select name="country_select[]" id="country_select_2" class="input-large" multiple>
								{foreach from=$countries.selected item='country'}
									<option value="{$country.id_country|intval}">&nbsp;{$country.name|escape}</option>
								{/foreach}
							</select>
							<a id="country_select_remove" class="btn btn-default btn-block clearfix"><i class="icon-arrow-left"></i> {l s='Remove' d='Admin.Actions'} </a>
						</td>
					</tr>
				</table>
			</div>
		{/if}

		{if ($carriers.unselected|@count) + ($carriers.selected|@count) > 1}
			<p class="checkbox">
				<label>
					<input type="checkbox" id="carrier_restriction" name="carrier_restriction" value="1" {if $carriers.unselected|@count}checked="checked"{/if} />
					{l s='Carrier selection' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<div id="carrier_restriction_div">
				<br />
				<table class="table">
					<tr>
						<td>
							<p>{l s='Unselected carriers' d='Admin.Catalog.Feature'}</p>
							<select id="carrier_select_1" class="input-large" multiple>
								{foreach from=$carriers.unselected item='carrier'}
									<option value="{$carrier.id_reference|intval}">&nbsp;{$carrier.name|escape}</option>
								{/foreach}
							</select>
							<a id="carrier_select_add" class="btn btn-default btn-block clearfix" >{l s='Add' d='Admin.Actions'} <i class="icon-arrow-right"></i></a>
						</td>
						<td>
							<p>{l s='Selected carriers' d='Admin.Catalog.Feature'}</p>
							<select name="carrier_select[]" id="carrier_select_2" class="input-large" multiple>
								{foreach from=$carriers.selected item='carrier'}
									<option value="{$carrier.id_reference|intval}">&nbsp;{$carrier.name|escape}</option>
								{/foreach}
							</select>
							<a id="carrier_select_remove" class="btn btn-default btn-block clearfix"><i class="icon-arrow-left"></i> {l s='Remove' d='Admin.Actions'} </a>
						</td>
					</tr>
				</table>
			</div>
		{/if}

		{if ($groups.unselected|@count) + ($groups.selected|@count) > 1}
			<p class="checkbox">
				<label>
					<input type="checkbox" id="group_restriction" name="group_restriction" value="1" {if $groups.unselected|@count}checked="checked"{/if} />
					{l s='Customer group selection' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<div id="group_restriction_div">
				<br />
				<table class="table">
					<tr>
						<td>
							<p>{l s='Unselected groups' d='Admin.Catalog.Feature'}</p>
							<select id="group_select_1" class="input-large" multiple>
								{foreach from=$groups.unselected item='group'}
									<option value="{$group.id_group|intval}">&nbsp;{$group.name|escape}</option>
								{/foreach}
							</select>
							<a id="group_select_add" class="btn btn-default btn-block clearfix" >{l s='Add' d='Admin.Actions'} <i class="icon-arrow-right"></i></a>
						</td>
						<td>
							<p>{l s='Selected groups' d='Admin.Catalog.Feature'}</p>
							<select name="group_select[]" class="input-large" id="group_select_2" multiple>
								{foreach from=$groups.selected item='group'}
									<option value="{$group.id_group|intval}">&nbsp;{$group.name|escape}</option>
								{/foreach}
							</select>
							<a id="group_select_remove" class="btn btn-default btn-block clearfix" ><i class="icon-arrow-left"></i> {l s='Remove' d='Admin.Actions'}</a>
						</td>
					</tr>
				</table>
			</div>
		{/if}

		{if ($cart_rules.unselected|@count) + ($cart_rules.selected|@count) > 0}
			<p class="checkbox">
				<label>
					<input type="checkbox" id="cart_rule_restriction" name="cart_rule_restriction" value="1" {if $cart_rules.unselected|@count}checked="checked"{/if} />
					{l s='Compatibility with other cart rules' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<div id="cart_rule_restriction_div">
				<br />
				<table  class="table">
					<tr>
						<td>
							<p>{l s='Uncombinable cart rules' d='Admin.Catalog.Feature'}</p>
							<input id="cart_rule_select_1_filter" autocomplete="off" class="form-control uncombinable_search_filter" type="text" name="uncombinable_filter" placeholder="{l s='Search' d='Admin.Actions'}" value="">
							<select id="cart_rule_select_1" class="jscroll" multiple="">
							</select>
							<a class="jscroll-next btn btn-default btn-block clearfix" href="">{l s='Next' d='Admin.Global'}</a>
							<a id="cart_rule_select_add" class="btn btn-default btn-block clearfix">{l s='Add' d='Admin.Actions'} <i class="icon-arrow-right"></i></a>
						</td>
						<td>
							<p>{l s='Combinable cart rules' d='Admin.Catalog.Feature'}</p>
							<input id="cart_rule_select_2_filter" autocomplete="off" class="form-control combinable_search_filter" type="text" name="combinable_filter" placeholder="{l s='Search' d='Admin.Actions'}" value="">
							<select name="cart_rule_select[]" class="jscroll" id="cart_rule_select_2" multiple>
							</select>
							<a class="jscroll-next btn btn-default btn-block clearfix" href="">{l s='Next' d='Admin.Global'}</a>
							<a id="cart_rule_select_remove" class="btn btn-default btn-block clearfix" ><i class="icon-arrow-left"></i> {l s='Remove' d='Admin.Actions'}</a>
						</td>
					</tr>
				</table>
			</div>
		{/if}

			<p class="checkbox">
				<label>
					<input type="checkbox" id="product_restriction" name="product_restriction" value="1" {if $product_rule_groups|@count}checked="checked"{/if} />
					{l s='Product selection' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<div id="product_restriction_div">
				<br />
				<table id="product_rule_group_table" class="table">
					{foreach from=$product_rule_groups item='product_rule_group'}
						{$product_rule_group}
					{/foreach}
				</table>
				<a href="javascript:addProductRuleGroup();" class="btn btn-default ">
					<i class="icon-plus-sign"></i> {l s='Product selection' d='Admin.Catalog.Feature'}
				</a>
			</div>

		{if ($all_shops|@count) > 1}
			<p class="checkbox">
				<label>
					<input type="checkbox" id="shop_restriction" name="shop_restriction" value="1" {if $shops.selected|@count || ($shops.selected|@count + $shops.unselected|@count < $all_shops|@count)}checked="checked"{/if} />
					{l s='Store selection' d='Admin.Catalog.Feature'}
				</label>
			</p>
			<div id="shop_restriction_div">
				<br/>
				<table class="table">
					<tr>
						<td>
							<p>{l s='Unselected shops' d='Admin.Catalog.Feature'}</p>
							<select id="shop_select_1" multiple>
								{foreach from=$shops.unselected item='shop'}
									<option value="{$shop.id_shop|intval}">&nbsp;{$shop.name|escape}</option>
								{/foreach}
							</select>
							<a id="shop_select_add" class="btn btn-default btn-block clearfix" >{l s='Add' d='Admin.Actions'} <i class="icon-arrow-right"></i></a>
						</td>
						<td>
							<p>{l s='Selected shops' d='Admin.Catalog.Feature'}</p>
							<select name="shop_select[]" id="shop_select_2" multiple>
								{foreach from=$shops.selected item='shop'}
									<option value="{$shop.id_shop|intval}">&nbsp;{$shop.name|escape}</option>
								{/foreach}
							</select>
							<a id="shop_select_remove" class="btn btn-default btn-block clearfix" ><i class="icon-arrow-left"></i> {l s='Remove' d='Admin.Actions'}</a>
						</td>
					</tr>
				</table>
			</div>
		{/if}
	</div>
</div>
