/*
 * OpenAPI Petstore
 * This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

package org.openapitools.model;

import java.util.Objects;
import java.util.Arrays;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import com.fasterxml.jackson.annotation.*;

import javax.validation.constraints.*;
import javax.validation.Valid;
import io.micronaut.core.annotation.*;
import javax.annotation.Generated;

/**
 * MapTest
 */
@JsonPropertyOrder({
  MapTest.JSON_PROPERTY_MAP_MAP_OF_STRING,
  MapTest.JSON_PROPERTY_MAP_OF_ENUM_STRING,
  MapTest.JSON_PROPERTY_DIRECT_MAP,
  MapTest.JSON_PROPERTY_INDIRECT_MAP
})
@JsonTypeName("MapTest")
@Generated(value="org.openapitools.codegen.languages.JavaMicronautClientCodegen")
@Introspected
public class MapTest {
    public static final String JSON_PROPERTY_MAP_MAP_OF_STRING = "map_map_of_string";
    private Map<String, Map<String, String>> mapMapOfString = null;

    /**
     * Gets or Sets inner
     */
    public enum InnerEnum {
        UPPER("UPPER"),
        LOWER("lower");

        private String value;

        InnerEnum(String value) {
            this.value = value;
        }

        @JsonValue
        public String getValue() {
            return value;
        }

        @Override
        public String toString() {
            return String.valueOf(value);
        }

        @JsonCreator
        public static InnerEnum fromValue(String value) {
            for (InnerEnum b : InnerEnum.values()) {
                if (b.value.equals(value)) {
                    return b;
                }
            }
            throw new IllegalArgumentException("Unexpected value '" + value + "'");
        }
    }
    public static final String JSON_PROPERTY_MAP_OF_ENUM_STRING = "map_of_enum_string";
    private Map<String, InnerEnum> mapOfEnumString = null;

    public static final String JSON_PROPERTY_DIRECT_MAP = "direct_map";
    private Map<String, Boolean> directMap = null;

    public static final String JSON_PROPERTY_INDIRECT_MAP = "indirect_map";
    private Map<String, Boolean> indirectMap = null;

    public MapTest() {
    }
    public MapTest mapMapOfString(Map<String, Map<String, String>> mapMapOfString) {
        this.mapMapOfString = mapMapOfString;
        return this;
    }

    public MapTest putMapMapOfStringItem(String key, Map<String, String> mapMapOfStringItem) {
        if (this.mapMapOfString == null) {
            this.mapMapOfString = new HashMap<String, Map<String, String>>();
        }
        this.mapMapOfString.put(key, mapMapOfStringItem);
        return this;
  }

    /**
     * Get mapMapOfString
     * @return mapMapOfString
     **/
    @Nullable
    @ApiModelProperty(value = "")
    @JsonProperty(JSON_PROPERTY_MAP_MAP_OF_STRING)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public Map<String, Map<String, String>> getMapMapOfString() {
        return mapMapOfString;
    }

    @JsonProperty(JSON_PROPERTY_MAP_MAP_OF_STRING)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public void setMapMapOfString(Map<String, Map<String, String>> mapMapOfString) {
        this.mapMapOfString = mapMapOfString;
    }

    public MapTest mapOfEnumString(Map<String, InnerEnum> mapOfEnumString) {
        this.mapOfEnumString = mapOfEnumString;
        return this;
    }

    public MapTest putMapOfEnumStringItem(String key, InnerEnum mapOfEnumStringItem) {
        if (this.mapOfEnumString == null) {
            this.mapOfEnumString = new HashMap<String, InnerEnum>();
        }
        this.mapOfEnumString.put(key, mapOfEnumStringItem);
        return this;
  }

    /**
     * Get mapOfEnumString
     * @return mapOfEnumString
     **/
    @Nullable
    @ApiModelProperty(value = "")
    @JsonProperty(JSON_PROPERTY_MAP_OF_ENUM_STRING)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public Map<String, InnerEnum> getMapOfEnumString() {
        return mapOfEnumString;
    }

    @JsonProperty(JSON_PROPERTY_MAP_OF_ENUM_STRING)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public void setMapOfEnumString(Map<String, InnerEnum> mapOfEnumString) {
        this.mapOfEnumString = mapOfEnumString;
    }

    public MapTest directMap(Map<String, Boolean> directMap) {
        this.directMap = directMap;
        return this;
    }

    public MapTest putDirectMapItem(String key, Boolean directMapItem) {
        if (this.directMap == null) {
            this.directMap = new HashMap<String, Boolean>();
        }
        this.directMap.put(key, directMapItem);
        return this;
  }

    /**
     * Get directMap
     * @return directMap
     **/
    @Nullable
    @ApiModelProperty(value = "")
    @JsonProperty(JSON_PROPERTY_DIRECT_MAP)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public Map<String, Boolean> getDirectMap() {
        return directMap;
    }

    @JsonProperty(JSON_PROPERTY_DIRECT_MAP)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public void setDirectMap(Map<String, Boolean> directMap) {
        this.directMap = directMap;
    }

    public MapTest indirectMap(Map<String, Boolean> indirectMap) {
        this.indirectMap = indirectMap;
        return this;
    }

    public MapTest putIndirectMapItem(String key, Boolean indirectMapItem) {
        if (this.indirectMap == null) {
            this.indirectMap = new HashMap<String, Boolean>();
        }
        this.indirectMap.put(key, indirectMapItem);
        return this;
  }

    /**
     * Get indirectMap
     * @return indirectMap
     **/
    @Nullable
    @ApiModelProperty(value = "")
    @JsonProperty(JSON_PROPERTY_INDIRECT_MAP)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public Map<String, Boolean> getIndirectMap() {
        return indirectMap;
    }

    @JsonProperty(JSON_PROPERTY_INDIRECT_MAP)
    @JsonInclude(value = JsonInclude.Include.USE_DEFAULTS)
       public void setIndirectMap(Map<String, Boolean> indirectMap) {
        this.indirectMap = indirectMap;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) {
            return false;
        }
        MapTest mapTest = (MapTest) o;
        return Objects.equals(this.mapMapOfString, mapTest.mapMapOfString) &&
            Objects.equals(this.mapOfEnumString, mapTest.mapOfEnumString) &&
            Objects.equals(this.directMap, mapTest.directMap) &&
            Objects.equals(this.indirectMap, mapTest.indirectMap);
    }

    @Override
    public int hashCode() {
        return Objects.hash(mapMapOfString, mapOfEnumString, directMap, indirectMap);
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("class MapTest {\n");
        sb.append("    mapMapOfString: ").append(toIndentedString(mapMapOfString)).append("\n");
        sb.append("    mapOfEnumString: ").append(toIndentedString(mapOfEnumString)).append("\n");
        sb.append("    directMap: ").append(toIndentedString(directMap)).append("\n");
        sb.append("    indirectMap: ").append(toIndentedString(indirectMap)).append("\n");
        sb.append("}");
        return sb.toString();
    }

    /**
     * Convert the given object to string with each line indented by 4 spaces
     * (except the first line).
     */
    private String toIndentedString(Object o) {
        if (o == null) {
            return "null";
        }
        return o.toString().replace("\n", "\n    ");
    }

}
