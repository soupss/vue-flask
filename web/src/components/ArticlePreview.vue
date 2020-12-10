<template>
    <p>{{ title }}</p>
    <small>({{ category }})</small>
    <p><b>{{ price }}$</b></p>
    <p>{{ created_at }}</p>
    <button @click="goToFullArticle">View full article</button>
</template>

<script>
export default {
    name: 'Article Preview',
    props: {
        title: String,
        description: String,
        price: Number,
        category: String,
        created_at: String,
        id: Number
    },
    methods: {
        goToFullArticle() {
            this.$router.push('/article/'+this.id)
        }
    }
}
</script>
