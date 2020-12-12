<template>
    <p>{{ title }}</p>
    <small>({{ category }})</small>
    <p><b>{{ price }}$</b></p>
    <p>{{ time_created }}</p>
    <button @click="goToArticlePage">View full article</button>
</template>

<script>
export default {
    name: 'Article Preview',
    props: {
        title: String,
        description: String,
        price: Number,
        category: String,
        time_created: String,
        id: Number
    },
    methods: {
        goToArticlePage() {
            this.$router.push('/articles/'+this.id)
        }
    }
}
</script>
