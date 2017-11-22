import axios from 'axios'
import qs from 'qs'
import omitBy from 'lodash/omitBy'

const client = axios.create({
  baseURL: process.env.BASE_API_URL
})

const formatParams = params => {
  return qs.stringify(
    omitBy(
      params,
      (param, key) =>
        typeof param === 'undefined' || param === null || param === ''
    )
  )
}

export const getCustomers = params => {
  const paramsString = formatParams(params)

  return client.get(`customers/?${paramsString}`)
}