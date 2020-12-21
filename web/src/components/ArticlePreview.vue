<template>
    <div class="mb-2 p-1 rounded border border-5 border-primary">
        <h3>{{ title }}</h3>
        <small>({{ category }})</small>
        <p><b>{{ price }}$</b></p>
        <p>{{ time_created }}</p>
        <button @click="goToArticlePage">View full article</button>
    </div>
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
