<template>
    <v-app>
        <v-app-bar app>
            <v-toolbar-title class="headline text-uppercase">
                <span>MyChess</span>
            </v-toolbar-title>
        </v-app-bar>

        <v-content>
            <Product name="Echiquier acajou et sycomore 44 cm avec notations"/>
            <Product name="Echiquier pliant acajou et sycomore 48 cm avec notations"/>
        </v-content>
    </v-app>
</template>

<script>

    import Product from './components/Chess';

    export default {
        name: 'App',
        components: {
            Product,
        },
        data: () => ({//
        }),
    };
</script>
