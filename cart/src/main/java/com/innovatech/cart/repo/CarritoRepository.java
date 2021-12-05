package com.innovatech.cart.repo;

import com.innovatech.cart.models.Carrito;
import org.springframework.data.mongodb.repository.MongoRepository;

import java.util.List;

public interface CarritoRepository extends MongoRepository<Carrito, String> {
    List<Carrito> findByUserId(String userId);

    Carrito findByProductId(String productId);

    Carrito findByProductIdAndUserId(String productId, String userId);
}
