<?php

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.

if (\class_exists(\ContainerVffbkmd\appDevDebugProjectContainer::class, false)) {
    // no-op
} elseif (!include __DIR__.'/ContainerVffbkmd/appDevDebugProjectContainer.php') {
    touch(__DIR__.'/ContainerVffbkmd.legacy');

    return;
}

if (!\class_exists(appDevDebugProjectContainer::class, false)) {
    \class_alias(\ContainerVffbkmd\appDevDebugProjectContainer::class, appDevDebugProjectContainer::class, false);
}

return new \ContainerVffbkmd\appDevDebugProjectContainer([
    'container.build_hash' => 'Vffbkmd',
    'container.build_id' => 'd5f324c9',
    'container.build_time' => 1636747431,
], __DIR__.\DIRECTORY_SEPARATOR.'ContainerVffbkmd');
