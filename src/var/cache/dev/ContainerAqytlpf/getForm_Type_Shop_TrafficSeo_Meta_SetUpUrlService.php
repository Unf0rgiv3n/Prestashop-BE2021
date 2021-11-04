<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'form.type.shop.traffic_seo.meta.set_up_url' shared service.

return $this->services['form.type.shop.traffic_seo.meta.set_up_url'] = new \PrestaShopBundle\Form\Admin\Configure\ShopParameters\TrafficSeo\Meta\SetUpUrlType(${($_ = isset($this->services['translator']) ? $this->services['translator'] : $this->getTranslatorService()) && false ?: '_'}, ${($_ = isset($this->services['prestashop.adapter.legacy.context']) ? $this->services['prestashop.adapter.legacy.context'] : $this->getPrestashop_Adapter_Legacy_ContextService()) && false ?: '_'}->getLanguages(), ${($_ = isset($this->services['prestashop.core.form.choice_provider.canonical_redirect_type']) ? $this->services['prestashop.core.form.choice_provider.canonical_redirect_type'] : $this->load('getPrestashop_Core_Form_ChoiceProvider_CanonicalRedirectTypeService.php')) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.core.util.url.url_file_checker']) ? $this->services['prestashop.core.util.url.url_file_checker'] : $this->load('getPrestashop_Core_Util_Url_UrlFileCheckerService.php')) && false ?: '_'}->isHtaccessFileWritable(), ${($_ = isset($this->services['prestashop.adapter.hosting_information']) ? $this->services['prestashop.adapter.hosting_information'] : ($this->services['prestashop.adapter.hosting_information'] = new \PrestaShop\PrestaShop\Adapter\Hosting\HostingInformation())) && false ?: '_'}->isHostMode(), ${($_ = isset($this->services['prestashop.adapter.tools']) ? $this->services['prestashop.adapter.tools'] : ($this->services['prestashop.adapter.tools'] = new \PrestaShop\PrestaShop\Adapter\Tools())) && false ?: '_'}->isModRewriteActive(), ${($_ = isset($this->services['prestashop.adapter.shop.shop_url']) ? $this->services['prestashop.adapter.shop.shop_url'] : $this->load('getPrestashop_Adapter_Shop_ShopUrlService.php')) && false ?: '_'}->doesMainShopUrlExist());
