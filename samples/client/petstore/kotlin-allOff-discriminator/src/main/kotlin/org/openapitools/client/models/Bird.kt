/**
 * Example
 *
 * An example
 *
 * The version of the OpenAPI document: 0.1
 * Contact: contact@example.org
 *
 * Please note:
 * This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * Do not edit this file manually.
 */

@file:Suppress(
    "ArrayInDataClass",
    "EnumEntryName",
    "RemoveRedundantQualifierName",
    "UnusedImport"
)

package org.openapitools.client.models

import org.openapitools.client.models.Animal

import com.squareup.moshi.Json

/**
 * 
 *
 * @param id 
 * @param featherType 
 */


data class Bird (

    @Json(name = "id")
    override val id: java.util.UUID,

    @Json(name = "featherType")
    val featherType: kotlin.String

) : Animal

