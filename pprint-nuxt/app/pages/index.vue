<script setup lang="ts">
import { useAccount, useEnsName } from "@wagmi/vue";

const { address } = useAccount();
const { data, error, status } = useEnsName({ address });
</script>

<template>
  <div v-if="status === 'pending'">Loading ENS name</div>
  <div v-else-if="status === 'error'">
    Error fetching ENS name: {{ error?.message }}
  </div>
  <div v-else>ENS name: {{ data }}</div>
</template>
