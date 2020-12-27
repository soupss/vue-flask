<template>
    <div class="m-2 shadow-lg rounded-3">
        <div class="d-flex justify-content-between bg-primary text-white rounded-top p-2">
            <span class="justify-content-start">
                <h3 class="mb-0">{{ article.title }}</h3>
            </span>
            <span class="ms-3 justify-content-end">
                <button class="btn btn-secondary me-2 h-100" @click="goToEditPage">
                    <i class="fas fa-pen fa-sm"></i>
                </button>
                <button class="btn btn-danger h-100" @click="deleteArticle">
                    <i class="fas fa-trash-alt fa-sm"></i>
                </button>
            </span>
        </div>
        <div class="rounded-bottom p-1">
            <p class="m-1 text-primary">
                <i class="m-1 fas fa-tshirt"></i>
                {{ article.category }}
            </p>
            <p class="m-1 text-info">
                <i class="m-1 fas fa-clock"></i>
                {{ article.time_created }}
            </p>
            <p class="m-1 text-success">
                <i class="m-1 fas fa-tag"></i>
                <span>{{ article.price }} kr</span>
            </p>
            <div class="text-center">
                <button class="btn btn-primary" @click="goToArticlePage">
                    View
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: 'Article Preview',
    props: {
            article: Object
    },
    methods: {
        goToArticlePage() {
            this.$router.push('/articles/'+this.article.id)
        },
        deleteArticle() {
            this.$store.dispatch('deleteArticle', this.article.id)
                .then(() => this.$parent.fetchArticles())
        },
        goToEditPage() {
            this.$router.push('/articles/' + this.article.id + '/edit')
        }
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    cursor: pointer;
}
a:hover {
    background-color: ;
}
p {
    margin-bottom: 0;
}
</style>
