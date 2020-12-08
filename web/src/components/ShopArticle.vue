<template>
    <h1>{{ title }}</h1>
    <small>{{ price }}$</small>
    <p>{{ description }}</p>
    <p>uploaded <b>{{ created_at }}</b></p>
</template>

<script>
export default {
    props: {
        title: String,
        description: String,
        price: Number,
        created_at: String,
        id: Number
    }
}
</script>
