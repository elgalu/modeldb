// THIS FILE IS AUTO-GENERATED. DO NOT EDIT
package ai.verta.modeldb.versioning.autogenerated._public.modeldb.versioning.model;

import java.util.*;
import java.util.function.Function;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import ai.verta.modeldb.ModelDBException;
import ai.verta.modeldb.versioning.*;
import ai.verta.modeldb.versioning.blob.diff.Function3;
import ai.verta.modeldb.versioning.blob.diff.*;
import ai.verta.modeldb.versioning.blob.visitors.Visitor;
import com.pholser.junit.quickcheck.generator.*;
import com.pholser.junit.quickcheck.generator.java.util.*;
import com.pholser.junit.quickcheck.random.*;

public class AutogenS3DatasetBlobGen extends Generator<AutogenS3DatasetBlob> {
    public AutogenS3DatasetBlobGen() {
        super(AutogenS3DatasetBlob.class);
    }

    @Override public AutogenS3DatasetBlob generate(
            SourceOfRandomness r,
            GenerationStatus status) {
                // if (r.nextBoolean())
                //     return null;

                AutogenS3DatasetBlob obj = new AutogenS3DatasetBlob();
                if (r.nextBoolean()) {
                    int size = r.nextInt(0, 10);
                    List<AutogenS3DatasetComponentBlob
> ret = new ArrayList(size);
                    for (int i = 0; i < size; i++) {
                        ret.add(gen().type(AutogenS3DatasetComponentBlob
.class).generate(r, status));
                    }
                    obj.setComponents(Utils.removeEmpty(ret));
                }
                return obj;
    }
}
