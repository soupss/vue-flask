<template>
    <div class="mt-2 rounded-3 shadow-lg">
        <div class="d-flex justify-content-between bg-primary text-white p-2 rounded-top">
            <span class="justify-content-start">
                <h1 class="mb-0">{{ article.title }}</h1>
            </span>
            <span class="justify-content-end">
                <button class="btn btn-secondary me-2 h-100" @click="goToEditPage">
                    <i class="ms-1 me-2 fas fa-pen fa-lg"></i>
                    <span class="fs-5">Edit</span>
                </button>
                <button class="btn btn-danger h-100" @click="deleteArticle">
                    <i class="ms-1 me-2 fas fa-trash-alt fa-lg"></i>
                    <span class="fs-5">Delete</span>
                </button>
            </span>
        </div>
        <div class="p-2">
            <p>uploaded <b>{{ article.time_created }}</b></p>
            <p>category:{{ article.category }}</p>
            <p>{{ article.price }}$</p>
        </div>
            <p>{{ article.description }}</p>
    </div>
</template>

<script>
export default {
    name: 'Article',
    props: {
        id: String
    },
    data() {
        return {
            article: {}
        }
    },
    methods: {
        deleteArticle() {
            this.$store.dispatch('deleteArticle', this.id)
                .then(() => this.$router.push('/articles'))
        },
        goToEditPage() {
            this.$router.push('/articles/' + this.id + '/edit')
        }
    },
    created() {
        this.$store.dispatch('fetchArticle', this.id)
            .then(response => (this.article = response))
    }

}
</script>
